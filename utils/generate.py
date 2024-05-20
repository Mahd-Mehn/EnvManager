from Crypto.PublicKey import RSA
import os

def generate_keys(save_location):
    # Generate RSA key pair
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Save in project folder (current working directory)
    project_folder = os.getcwd()

    if save_location == "project_folder":

        private_key_path = os.path.join(project_folder, "private.pem")
        public_key_path = os.path.join(project_folder, "public.pem")

        # Write the private key to file
        with open(private_key_path, "wb") as prv_file:
            prv_file.write(private_key)
        # Write the public key to file
        with open(public_key_path, "wb") as pub_file:
            pub_file.write(public_key)

        # Append "*.pem" to .gitignore
        gitignore_path = os.path.join(project_folder, ".gitignore")
        with open(gitignore_path, "a") as gitignore_file:
            gitignore_file.write("\nprivate.pem\n")

        print("RSA key pair generated and saved in the project folder.")
    elif save_location == "ssh_folder":
        # Save in ~/.ssh/ folder
        private_key_path = os.path.expanduser("~/.ssh/private.pem")
        public_key_path = os.path.expanduser("~/.ssh/public.pem")

        # Write the private key to file
        with open(private_key_path, "wb") as prv_file:
            prv_file.write(private_key)
        # Write the public key to file
        with open(public_key_path, "wb") as pub_file:
            pub_file.write(public_key)

        print("RSA key pair generated and saved in ~/.ssh/ folder.")
    else:
        print("Invalid save location. Please choose 'project_folder' or 'ssh_folder'.")
