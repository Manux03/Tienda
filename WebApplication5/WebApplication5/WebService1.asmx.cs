using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace WebApplication5
{
    /// <summary>
    /// Descripción breve de WebService1
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // Para permitir que se llame a este servicio web desde un script, usando ASP.NET AJAX, quite la marca de comentario de la línea siguiente. 
    // [System.Web.Script.Services.ScriptService]
    public class WebService1 : System.Web.Services.WebService
    {

        [WebMethod]
        public DataSet WSConsulta()
        {
            string sConnectionString;
            sConnectionString = "server=localhost;uid=root;pwd=123456;database=tienda";
            MySqlConnection objconn = new MySqlConnection(sConnectionString);
            objconn.Open();
            MySqlDataAdapter da = new MySqlDataAdapter("select * from core_producto", objconn);
            DataSet ds = new DataSet("producto");
            da.FillSchema(ds, SchemaType.Source, "producto");
            da.Fill(ds, "persona");
            return ds;
        }
        [WebMethod]
        public DataSet WSBusca(int idProducto)
        {
            string sConnectionString;
            sConnectionString = "server=localhost;uid=root;pwd=123456;database=tienda";
            MySqlConnection objconn = new MySqlConnection(sConnectionString);
            objconn.Open();
            MySqlDataAdapter da = new MySqlDataAdapter("select * from core_producto where idProducto='" + idProducto + "'", objconn);
            DataSet ds = new DataSet("producto");
            da.FillSchema(ds, SchemaType.Source, "producto");
            da.Fill(ds, "persona");
            return ds;
        }
        [WebMethod]
        public void WSInsert (int idProducto, string nombreProducto, int precio , int stock, string marca , string modelo, string imagen, string descripcion)
        {
            string sConnectionString;
            sConnectionString = "server=localhost;uid=root;pwd=123456;database=tienda";
            string sql = "INSERT INTO core_producto (idProducto, nombreProducto, precio, stock, marca, modelo, descripcion, imagen) VALUES ('" + idProducto + "', '" + nombreProducto + "','" + precio + "','" + stock + "','" + marca + "','" + modelo +"','" + descripcion + "','" + imagen + "')";
            MySqlConnection objconn = new MySqlConnection(sConnectionString);
            objconn.Open();

            MySqlCommand comando = new MySqlCommand(sql, objconn);
            comando.ExecuteNonQuery();

        }

        [WebMethod]
        public void WSDelete (int idProducto)
        {
            string sConnectionString;
            sConnectionString = "server=localhost;uid=root;pwd=123456;database=tienda";
            string sql = "DELETE FROM core_producto WHERE idProducto= ('" + idProducto +"')";
            MySqlConnection objconn = new MySqlConnection(sConnectionString);
            objconn.Open();

            MySqlCommand comando = new MySqlCommand(sql, objconn);
            comando.ExecuteNonQuery();

        }

        [WebMethod]
        public void WSUpdate(int idProductobusqueda, int idProducto, string nombreProducto, int precio, int stock, string marca, string modelo, string imagen, string descripcion)
        {
            string sConnectionString;
            sConnectionString = "server=localhost;uid=root;pwd=123456;database=tienda";
            string sql = "UPDATE core_producto SET idProducto='" + idProducto + "', nombreProducto='" + nombreProducto + "', precio='" + precio + "', stock='" + stock + "', marca='" + marca + "', modelo='" + modelo + "', descripcion='" + descripcion + "', imagen='" + imagen + "' WHERE idProducto='" + idProductobusqueda + "'";
            MySqlConnection objconn = new MySqlConnection(sConnectionString);
            objconn.Open();

            MySqlCommand comando = new MySqlCommand(sql, objconn);
            comando.ExecuteNonQuery();

        }
    }
}