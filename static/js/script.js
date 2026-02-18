document.addEventListener('DOMContentLoaded', () => {
    const readmeForm = document.getElementById('readme-form');
    const recentGrid = document.getElementById('recent-grid');

    // Handle Form Submission
    if (readmeForm) {
        readmeForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = readmeForm.querySelector('button[type="submit"]');
            const loader = submitBtn.querySelector('.loader');
            const btnText = submitBtn.querySelector('.btn-text');

            // Show Loading
            loader.style.display = 'inline-block';
            btnText.textContent = 'Generating...';
            submitBtn.disabled = true;

            const formData = {
                project_name: document.getElementById('project_name').value,
                description: document.getElementById('description').value,
                features: document.getElementById('features').value,
                installation: document.getElementById('installation').value,
                usage: document.getElementById('usage').value,
                tech_stack: document.getElementById('tech_stack').value,
                author: document.getElementById('author').value,
                github_link: document.getElementById('github_link').value
            };

            try {
                const response = await fetch('/api/generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData)
                });

                const result = await response.json();
                if (result.success) {
                    window.location.href = `/result/${result.id}`;
                } else {
                    alert('Error: ' + result.error);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while generating the README.');
            } finally {
                loader.style.display = 'none';
                btnText.textContent = 'Generate README';
                submitBtn.disabled = false;
            }
        });
    }

    // Fetch Recent READMEs
    if (recentGrid) {
        fetchRecentReadmes();
    }

    async function fetchRecentReadmes() {
        try {
            const response = await fetch('/api/recent');
            const data = await response.json();

            recentGrid.innerHTML = data.length ? '' : '<p style="text-align:center; grid-column: 1/-1; opacity: 0.5;">No READMEs generated yet.</p>';

            data.forEach(item => {
                const card = document.createElement('div');
                card.className = 'glass recent-card';
                card.innerHTML = `
                    <h3 style="margin-bottom: 0.5rem">${item.project_name}</h3>
                    <p style="font-size: 0.8rem; margin-bottom: 1.5rem; opacity: 0.7;">Generated on ${item.timestamp}</p>
                    <a href="/result/${item.id}" class="btn btn-primary" style="padding: 0.6rem 1.2rem; font-size: 0.9rem">View README</a>
                `;
                recentGrid.appendChild(card);
            });
        } catch (error) {
            console.error('Error fetching recent:', error);
        }
    }
});

// Copy to Clipboard
function copyToClipboard() {
    const markdownText = document.getElementById('markdown-raw').value;
    navigator.clipboard.writeText(markdownText).then(() => {
        const copyBtn = document.getElementById('copy-btn');
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
        setTimeout(() => {
            copyBtn.innerHTML = originalText;
        }, 2000);
    });
}

// In-page Regeneration
async function regenerateReadme(recordId) {
    const regenBtn = document.getElementById('regenerate-btn');
    const regenText = document.getElementById('regen-text');
    const previewArea = document.getElementById('markdown-preview');
    const rawArea = document.getElementById('markdown-raw');

    // Show Loading
    regenBtn.disabled = true;
    const originalText = regenText.textContent;
    regenText.textContent = 'Generating...';
    previewArea.style.opacity = '0.5';

    try {
        const response = await fetch(`/api/regenerate/${recordId}`, {
            method: 'POST'
        });

        const result = await response.json();
        if (result.success) {
            // Update Preview
            rawArea.value = result.content;
            previewArea.innerHTML = marked.parse(result.content);
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during regeneration.');
    } finally {
        regenBtn.disabled = false;
        regenText.textContent = originalText;
        previewArea.style.opacity = '1';
    }
}
