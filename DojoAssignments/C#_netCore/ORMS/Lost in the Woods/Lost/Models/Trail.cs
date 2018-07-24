using System.ComponentModel.DataAnnotations;
namespace Lost.Models

{
    public class Trail
    {
        [Required]
        public string name {get;set;}
        [Required]
        [MinLength(10)]
        public string desc {get;set;}
        [Required]
        [Range(0,double.MaxValue)]
        public int length {get;set;}
        [Required]
        [Range(0,double.MaxValue)]
        public int elevation {get;set;}
        [Required]
        [Range(0,double.MaxValue)]
        public int longtitude {get;set;}
        [Required]
        [Range(0,double.MaxValue)]
        public int latitude {get;set;}
        
    }
}