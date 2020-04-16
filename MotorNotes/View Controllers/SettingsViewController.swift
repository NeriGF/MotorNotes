//
//  SettingsViewController.swift
//  MotorNotes
//
//  Created by Jonathon Chenvert on 4/16/20.
//  Copyright © 2020 Jonathon Chenvert. All rights reserved.
//

import UIKit
import FirebaseAuth

class SettingsViewController: UIViewController {
    
    let userDefault = UserDefaults.standard

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBAction func logoutTapped(_ sender: Any) {
        
        do {
            // Sign user out
            try Auth.auth().signOut()
            Constants.authPersistence(false)
        
            // Return to login page
            transitionToLogin()
        } catch let error {
            print("Error signing out of Firebase:\n\(error.localizedDescription)")
        }
    }
    
    func transitionToLogin() {
        
        // Return to login view controller
        let loginViewController = storyboard?.instantiateViewController(identifier: Constants.Storyboard.loginViewController) as? LoginViewController
        
        view.window?.rootViewController = loginViewController
        view.window?.makeKeyAndVisible()
    }
}
