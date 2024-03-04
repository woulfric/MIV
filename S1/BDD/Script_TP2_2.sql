--1.Connectez vous avec l’utilisateur DBAINTERVENTION et créez un autre utilisateur : Admin.

--connexion avec dbaintervention et création de l'utilisateur admin

connect dbaintervention/psw
(pour la version 19 excuter d'abord Alter session...)

create user admin identified by psw default tablespace intervention_tbs temporary tablespace intervention_temptbs;

--verfier que admin est créé,  on accède à la vue dba_users via l'utilisateur system

connect system/pswd

desc dba_users -- cette vue contient tous les utilisateurs de le SGBD oracle

select username from dba_users where username=upper('admin');--upper convertit une chaine en entrée en une chaine majuscule

--2.	Connectez-vous à l’aide cet utilisateur. Que remarquez-vous ?

connect admin/psw

--Remarque :    Nous remarquons que nous ne pouvons pas se connecter à l'aide de cet utilisateur car il n'a pas les privilèges nécessaires (create session) pour connecter   Erreur : privilèges insuffisants.

-- 3. Donner le droit de création d’une session pour cet utilisateur (Create Session) et reconnecter

--accorder le privilège de connexion a admin à partir de l'utilisateur dbaintervention

connect dbaintervention/psw

grant create session to admin;

-- verifier à partir de catalogue oracle que l'utilisateur a le privilège

connect system/pswd

select privilege, admin_option from dba_sys_privs where grantee='ADMIN';--dba_sys_privs contient tous les privilèges systèmes

connect admin/psw

select privilege, admin_option from user_sys_privs;--user_sys_privs contient tous les privilèges systèmes de l'utilisateur connecté

---4.	Donner les privilèges suivants à Admin: créer des tables, des utilisateurs. Vérifier.

connect dbaintervention/psw

grant create user, create table, create view to admin;

(pour la version 19 si ça ne marche pas sous dbaintervention connectez vous : conn sys as sysdba et executer après le grant)

--vérification

connect system/pswd

select privilege, admin_option from dba_sys_privs where grantee='ADMIN';

connect admin/psw

select privilege, admin_option from user_sys_privs;

--création d'une table

create table test (a integer, b char(1));

--pas de quota sur le tablespace intervention_tbs, donc il faut lui accorder un quota

connect DBAINTERVENTION/psw

alter user admin  quota unlimited on intervention_tbs;

connect admin/psw

create table test (a integer, b char(1));

--Vérification sur le catalogue:

select table_name from tabs;

insert into test values (1, 'b');-- Il est le proporietaire de la table 

select * from test;-- Il est le proporietaire de la table 

--Vérification sur le catalogue:

select object_name, object_type from user_objects;--retrouver les objets de l'utilisateur connecté

--création d'une vue

create view view1 as select a from test;

--verifier
select * from view1;

select object_name, object_type from user_objects;

connect system/pswd;
desc dba_objects;
select owner, object_name, object_type from dba_objects where owner='ADMIN';


--création d'un autre utilisateur

connect admin/psw

create user user_test identified by psw;

--Vérification sur le catalogue:

connect system/pswd
select username, default_tablespace, temporary_tablespace, password, profile from dba_users where username =upper('user_test');

--5.	Exécutez la requête Q1 suivante : Select * from  DBAINTERVENTION.EMPLOYE ; Que remarquez-vous ?

connect admin/psw
Select * from  DBAINTERVENTION.EMPLOYE;

-- resultat: ORA-00942: Table ou vue inexistante

-- 6. Donner les droits de lecture à cet utilisateur pour la table employe.

--accorder le privilège de select sur la table employe

connect dbaintervention/psw
grant select on employe to admin;

--verfier à partir de catalogue la transmission de privilège, il faut accèder à la vue dba_tab_privs contenant tous les privilèges objets

connect system/psw
 select grantee, owner, table_name, privilege, grantable from dba_tab_privs where grantee='ADMIN';

 connect admin/psw
 select * from dbaintervention.employe;

 --7.	Le centre de gestion des interventions augmente les salaires des employés dont le nombre total des interventions est supérieur à 5 par 5000 DA . Que faut-il faire ? Que remarquez-vous ?

 connect admin/psw
 update dbaintervention.employe
 set salaire=salaire+5000
 where numemploye in(
 select numemploye
 from dbaintervention.intervenants
 group by numemploye having count(*)>=2);

select numemploye from intervenants having count(*)>=2 group by numemploye;

 -- resultat: ORA-01031: privilèges insuffisants

 --8.	Donner les droits de mise à jour  à  cet utilisateur pour la table EMPLOYE, les droits de lecture sur la table INTERVENANTS et réessayer de refaire la modification.
 --accorder le privilège de update sur la table employe et select sur intervenants

 connect dbaintervention/psw

 grant update on employe to admin;
 grant select on intervenants to admin;

 --verfier à partir de catalogue la transmission de privilège, il faut accèder à la vue dba_tab_privs

connect system/psw
 select grantee, owner, table_name, privilege, grantable from dba_tab_privs where grantee='ADMIN';

 --execution à partir de admin

 connect admin/psw
 update dbaintervention.employe
 set salaire=salaire+5000
 where numemploye in(
 select numemploye
 from dbaintervention.intervenants
 group by numemploye having count(*)>5);

 --Créer un index NOMEMP_IX sur l’attribut NOMEMP de la table EMPLOYE. Que remarquez-vous ?

 connect admin/psw
 create index NOMEMP_IX  on dbaintervention.employe(nomemp);

 --résultat: pas de privilège

 --  Donner les droits de création d’index à admin pour la table employe

  connect dbaintervention/psw
grant index on employe to admin;

--vérification

connect system/pswd
select grantee, owner, table_name, privilege, grantable from dba_tab_privs where grantee='ADMIN';

connect admin/psw
create index NOMEMP_IX on dbaintervention.employe(nomemp);

--resultat: Index créé.

select object_name from user_objects;

-- 11. Enlever les privilèges précédemment accordés.

connect dbaintervention/psw
--privilège système
revoke create session, create user, create table, create view from admin;

--vérification
connect system/psw
select privilege , admin_option from dba_sys_privs where grantee=upper('admin');

connect dbaintervention/psw

--privilège objet

revoke select, update, index on employe from admin;
revoke select on intervenants from admin;

--vérification
connect system/pswd

select privilege, admin_option from dba_sys_privs where grantee='ADMIN';
select grantee,owner, grantor, table_name, privilege from dba_tab_privs where grantee=upper('admin');

--Créer un profil « Interv_Profil » qui est caractérisé par : (  3 sessions simultanés autorises, Un appel système ne peut pas consommer plus de 35 secondes de CPU,  Chaque session ne peut excéder 90 minutes,  Un appel système ne peut lire plus de 1200 blocs de donnes en mémoire et sur le disque,  Chaque session ne peut allouer plus de 25 ko de mémoire en SGA,  Pour chaque session, 30 minutes d’inactivité maximum sont autorisés,  5 tentatives de connexion avant blocage du compte,  Le mot de passe est valable pendant 50 jours et il faudra attendre 40 jours avant qu’il puisse être utilisé à  nouveau,  1 seul jour d’interdiction d’accès après que les 5 tentatives de connexion ont été atteintes,  La période de grâce qui prolonge l’utilisation du mot de passe avant son changement est de 5 jours).

connect dbaintervention/psw

create profile Interv_Profil limit
sessions_per_user 3
cpu_per_call 3500
connect_time 90
logical_reads_per_session 1200
private_sga 25K
idle_time 30
failed_login_attempts 5
password_lock_time 1
password_life_time 50
password_reuse_time 40
password_reuse_max unlimited
password_grace_time 5;

--vérification

connect system/pswd

select * from dba_profiles where profile=upper('Interv_Profil');
select * from dba_profiles where profile=upper('Interv_Profil') and limit <>'DEFAULT';


-- 14. Affecter ce profil à l’utilisateur admin

connect dbaintervention/psw
alter user admin profile Interv_Profil;

--vérification

connect system/pswd
select username, profile from dba_users where username=upper('admin'); 

-- 15.Créer le rôle : « GESTIONNAIRE_DES_INTERVENTIONS » qui peut voir les tables EMPLOYE, VEHICULE, CLIENT et peut modifier les tables INTERVENTIONS et INTERVENANTS.

connect dbaintervention/psw

create role GESTIONNAIRE_DES_INTERVENTIONS;

connect system/pswd

select role from dba_roles where role='GESTIONNAIRE_DES_INTERVENTIONS';

connect dbaintervention/psw

grant select on EMPLOYE to GESTIONNAIRE_DES_INTERVENTIONS;
grant select on VEHICULE to GESTIONNAIRE_DES_INTERVENTIONS;
grant select on CLIENT to GESTIONNAIRE_DES_INTERVENTIONS;
grant update on INTERVENTIONS to GESTIONNAIRE_DES_INTERVENTIONS;
grant update on INTERVENANTS to GESTIONNAIRE_DES_INTERVENTIONS;

---vérifier

select USERNAME, GRANTED_ROLE from user_role_privs;

Comme c’est des privilèges objet qu’on a mis dans ce rôle, on consulte user_tab_pris: 

select privilege, table_name from user_tab_privs where grantee='GESTIONNAIRE_DES_INTERVENTIONS';


-- 16. Assigner ce rôle à admin. Vérifier que les autorisations assignées au rôle GESTIONNAIRE_DES_INTERVENTIONS, ont été bien transférées sur l’utilisateur admin.

connect dbaintervention/psw
grant GESTIONNAIRE_DES_INTERVENTIONS to admin;

--vérification
connect system/pswd
select * from dba_role_privs where GRANTEE =upper('admin');
