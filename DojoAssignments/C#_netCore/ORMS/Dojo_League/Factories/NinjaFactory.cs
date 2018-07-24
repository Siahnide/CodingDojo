using System;
using System.Data;
using Dojo_League.Models;
using System.Collections.Generic;
using MySql.Data.MySqlClient;
using Dapper;
using System.Linq;

namespace NinjaFactory.Factories
{
public class DbConnector
        {
                static string server = "localhost";
                static string db = "leaguedb"; //Change to your schema name
                static string port = "3306"; //Potentially 8889
                static string user = "root";
                static string pass = "0000003342";
                internal static IDbConnection Connection {
                        get {
                                return new MySqlConnection($"Server={server};Port={port};Database={db};UserID={user};Password={pass};SslMode=None");
                        }
                }

        public static void AddNewNinja(Ninja ninja)
        {
             using(IDbConnection dbConnection = Connection)
                {
                    string query = $" INSERT INTO ninjas (name,level,description,dojo) VALUES('{ninja.name}','{ninja.level}','{ninja.description}','{ninja.dojo}')";
                    dbConnection.Open();
                    dbConnection.Execute(query);
                }
        }
 

        public static IEnumerable<Ninja> SelectNinjas()
        {
                using(IDbConnection dbConnection = Connection)
                {
                        string query = "SELECT * FROM ninjas";
                        return dbConnection.Query<Ninja>(query);
                }
        }
        public static Ninja SelectNinjas(int id)
        {
                using(IDbConnection dbConnection = Connection)
                {
                        string query = $"SELECT * FROM ninjas WHERE id='{id}'";
                        return dbConnection.Query<Ninja>(query).First();
                }
        }
        public static void AddNewDojo(Dojo dojo)
        {
             using(IDbConnection dbConnection = Connection)
                {
                    string query = $" INSERT INTO dojos (name,location,info) VALUES('{dojo.name}','{dojo.location}','{dojo.info}')";
                    dbConnection.Open();
                    dbConnection.Execute(query);
                }
        }

        public static IEnumerable<Dojo> SelectDojos()
        {
                using(IDbConnection dbConnection = Connection)
                {
                        string query = "SELECT * FROM dojos";
                        return dbConnection.Query<Dojo>(query);
                }
        }
        public static Dojo SelectDojos(int id)
        {
                using(IDbConnection dbConnection = Connection)
                {
                        string query = $"SELECT * FROM dojos WHERE id='{id}'";
                        IEnumerable<Dojo> dojos = dbConnection.Query<Dojo>(query);
                        Dojo dojo = dojos.First();
                        return dojo;
                }
        }
        public static IEnumerable<Ninja> NinjasFromDojo(int id)
        {
                using(IDbConnection dbConnection = Connection)
                {
                string query =$"SELECT * FROM ninjas WHERE dojo = '{id}'";
                
                return dbConnection.Query<Ninja>(query);
                }
        }
        public static IEnumerable<Ninja> RogueNinjas()
        {
                using(IDbConnection dbConnection = Connection)
                {
                        string query = $"SELECT * FROM ninjas WHERE dojo = 0";
                        return dbConnection.Query<Ninja>(query);
                }
        }

        public static void JoinDojo( int dojo_id,int ninja_id)
        {
                using(IDbConnection dbConnection = Connection)
                {
                        string query = $"UPDATE ninjas SET dojo = '{dojo_id}' WHERE id='{ninja_id}'";
                        dbConnection.Query(query);
                }
        }
        public static void Banish(int ninja_id)
        {
                using(IDbConnection dbConnection = Connection)
                {
                        string query = $"UPDATE ninjas SET dojo = '{0}' WHERE id='{ninja_id}'";
                        dbConnection.Query(query);
                }
        }
        // public static Dojo TranslateDojo(int id)
        // {
        //         using(IDbConnection dbConnection = Connection)
        //         {
        //                 string query =$"SELECT * FROM dojos WHERE id = '{id}'";
        //                 IEnumerable<Dojo> dojos = dbConnection.Query<Dojo>(query);
        //                 return dojos.First();

        //         }
        // }
    }
}