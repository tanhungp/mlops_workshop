from matplotlib import pyplot as plt

def fig1_team_skills():
    skills = ['Software', 'AI', 'Domain']

    ai_scientist = [1, 4, 5]

    research_engineer = [1/3, 1/3, 1/3]

    software_engineer = [6, 3, 1]


    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10,4), dpi=120)

    fig.suptitle('Expertise of different roles')
    _ = ax1.pie(ai_scientist, startangle=0)
    ax1.set_title('AI Scientist')
    _ = ax2.pie(research_engineer, startangle=-60)
    ax2.set_title('Research Engineer')
    _ = ax3.pie(software_engineer, startangle=-145)
    ax3.set_title('Software Engineer')

    handles, labels = ax3.get_legend_handles_labels()
    _ = fig.legend(labels=skills, loc='upper left')
