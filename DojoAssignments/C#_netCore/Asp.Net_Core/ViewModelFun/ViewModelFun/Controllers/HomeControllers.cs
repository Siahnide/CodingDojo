using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using ViewModelFun.Models;
using System.Collections.Generic;
namespace ViewModelFun.Controllers
{
    public class HomeControllers : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult index()
        {
            message msg= new message()
            {
             content = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aut ipsa aspernatur reiciendis error magni fugit facere officia, alias expedita! Aperiam, corporis."

            };
            return View(msg);
        }
        [HttpGet]
        [Route("number")]
        public IActionResult number()
        {
            
            numbers num = new numbers()
            {
                all = new int[] {1,2,3}
            };
            
            return View(num);
        }
        [HttpGet]
        [Route("users")]
        public IActionResult users()
        {
            user dude = new user()
            {
                FirstName = "Bobby",
                LastName = "Jones"
            };
            user dudette = new user()
            {
                FirstName = "Berly",
                LastName = "Jersned"
            };   

            List<user> dudes = new List<user>();
            dudes.Add(dude);
            dudes.Add(dudette);

            users dudeses = new users(){
                people = new List<user>()
            };
            dudeses.people.Add(dude);
            dudeses.people.Add(dudette);
            return View(dudeses);
        }
        [HttpGet]
        [Route("user")]
        public IActionResult user()
        {
            user dude = new user()
            {
                FirstName = "Bobby",
                LastName = "Jones"
            };
            user dudette = new user()
            {
                FirstName = "Berly",
                LastName = "Jersned"
            };

            return View(dude);
        }
    }
}