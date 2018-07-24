using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Quoting_Dojo.Models;
using DbConnection;

namespace Quoting_Dojo.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Index()
        {
            return View();
        }
        [HttpPost("quotes")]
        public IActionResult Quotes(string name, string quote)
        {
  
            string query = $"INSERT into Quotes (name,quote,created_at) VALUES('{name}','{quote}',NOW())";
            DbConnector.Query(query);
            
            
            return RedirectToAction("quotes");
        }    


        [HttpGet("quotes")]
        public IActionResult quotes()
        {
            string list = "SELECT * FROM Quotes ORDER BY created_at DESC";
            ViewBag.list = DbConnector.Query(list);
            return View("Quotes");
        }
    }
}
