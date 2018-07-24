using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using rpg.Models;
using DbConnection;

namespace rpg.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            var users = DbConnector.Query("SELECT * FROM Users");
            ViewBag.Users = users;
            return View();
        }
    }
}
