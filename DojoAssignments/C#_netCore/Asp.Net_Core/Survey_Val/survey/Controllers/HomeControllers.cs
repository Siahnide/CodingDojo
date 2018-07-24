using Microsoft.AspNetCore.Mvc;
using survey.Models;
using System;
namespace survey.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }
        
        [HttpPost("Create")]
        public IActionResult Create(User user)
        {
            if(ModelState.IsValid)
            {
                User us = new User()
                {
                    Name=user.Name,
                    Location=user.Location,
                    Language=user.Language,
                    Comment=user.Comment
                };
                return View(user);
            }
            else
            {
                
                return View("Index");
            }
        }
    }
}