using Microsoft.AspNetCore.Http;
using System.ComponentModel.DataAnnotations;


namespace Orpg.Models
{
    public class User
    {
        [Required]
        public string username {get; set;}
        [Required]
        [EmailAddress]
        public string email {get; set;}
        [Required]
        public string password {get; set;}

    }
}