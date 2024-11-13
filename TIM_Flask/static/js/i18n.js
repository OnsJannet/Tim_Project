const translations = {
  en: {
    translation: {
      financial_plan_title: "Financial Business Plan",
      profile: "Profile",
      logout: "Logout",
      dashboard: "Dashboard",
      external_activities: "External Workshop Activities",
      access_visibility: "Access & Visibility",
      Acces: "Access",
      Visibility: "Visibility",
      good_morning: "Good Morning",
      admin: "Admin",
      add_version: "Add a Version",
      add_new_version: "Add a new Version",
      verions_name: "Version Name",
      Confirm_deletion: "Confirm Deletion",
      Warning_deletion:
        "Once you delete something, there is no going back. Be sure.",
      turnover: "Turnover",
      external: "External",
      oils_and_lubricants: "Oils and Lubricants",
      outsourced_workshop_activities: "Outsourced workshop activities",
      Internal: "Internal",
      total_change: "Total change",
      cost_of_sales: "Cost of sales",
      salaries_and_wages: "Salaries and wages",
      // Add other keys following this pattern
    },
  },
  fr: {
    translation: {
      financial_plan_title: "Plan d'affaires financier",
      profile: "Profil",
      logout: "Déconnexion",
      dashboard: "Tableau de bord",
      external_activities: "Activités d'atelier externalisées",
      access_visibility: "Accès & visibilité",
      Acces: "Accès",
      Visibilité: "Visibilité",
      good_morning: "Bonjour",
      admin: "Admin",
      add_version: "Ajouter une version",
      add_new_version: "Ajouter une nouvelle version",
      version_name: "Nom de la version",
      Confirm_deletion: "Confirmer la suppression",
      Warning_deletion:
        "Une fois que vous supprimez quelque chose, il n'y a pas de retour en arrière. Soyez certain.",
      turnover: "Chiffre d'affaires",
      external: "Externe",
      oils_and_lubricants: "Huiles & Lubrifiants",
      outsourced_workshop_activities: "Activités d'atelier externalisées",
      Internal: "Interne",
      total_change: "Changement total",
      cost_of_sales: "Coût des ventes",
      salaries_and_wages: "Salaires et rémunérations",
      // Add other keys following this pattern
    },
  },
};

document.addEventListener("DOMContentLoaded", function () {
  i18next
    .use(window.i18nextBrowserLanguageDetector) // Assumes `i18next-browser-languagedetector` is loaded
    .init(
      {
        resources: translations,
        fallbackLng: "en",
        debug: true,
      },
      function (err) {
        if (err) {
          console.error("i18next initialization error:", err);
        } else {
            console.log("Current language:", i18next.language);
          updateContent(); // Call updateContent only after i18next has initialized
        }
      }
    );
});

// Function to update content based on selected language
function updateContent() {
  document.title = i18next.t("financial_plan_title") + " - Tim";

  const elements = {
    financial_plan_title: "financial_plan_title",
    good_morning: "good_morning",
    profile: "profile",
    profile_link: "profile-link",
    logout_link: "logout-link",
    dashboard: "dashboard",
    external_activities: "external-activities",
    access_visibility: "access_visibility",
    access: "Acces",
    visibility: "Visibility",
    admin: "admin",
    add_version: "add_version",
    add_new_version: "add_new_version",
    versions_name: "verions_name",
    confirm_deletion: "Confirm_deletion",
    warning_deletion: "Warning_deletion",
    turnover: "turnover",
    external: "external",
    oils_and_lubricants: "oils_and_lubricants",
    outsourced_workshop_activities: "outsourced_workshop_activities",
    internal: "Internal",
    total_change: "total_change",
    cost_of_sales: "cost_of_sales",
    salaries_and_wages: "salaries_and_wages"
  };

  for (const [key, elementId] of Object.entries(elements)) {
    const element = document.getElementById(elementId);
    if (element) {
      element.textContent = i18next.t(key);
    } else {
      console.warn(`Element with ID '${elementId}' not found.`);
    }
  }
}

export default updateContent;
