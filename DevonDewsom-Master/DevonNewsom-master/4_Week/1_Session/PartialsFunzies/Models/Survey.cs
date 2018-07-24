using System.ComponentModel.DataAnnotations;
namespace PartialsFunzies.Models
{
    public class Survey
    {
        [Required]
        [Display(Name="Nombre")]
        public string Name {get;set;}
        [Required]
        [MaxLength(20)]

        public string Location {get;set;}
        // TODO: Validatie Langage so that it must be contained in GetLanguages()
        public string Language {get;set;}
        public static string[] GetLanguages()
        {
            return new string[]
            {
                "C#", "C++", "Golang", "Mandarin (Traditional)", "Spanish"
            };
        }
    }
}