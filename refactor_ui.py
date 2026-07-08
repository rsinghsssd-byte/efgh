import os

target = 'templates/blogs/edit_blog.html'

with open(target, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update overall cards
old_card = "bg-white dark:bg-slate-900 rounded-2xl shadow border p-6"
new_card = "bg-white/80 dark:bg-slate-900/80 backdrop-blur-xl rounded-3xl shadow-[0_8px_30px_rgb(0,0,0,0.04)] dark:shadow-[0_8px_30px_rgb(0,0,0,0.1)] border border-slate-200/50 dark:border-slate-700/50 p-8 hover:shadow-xl transition-all duration-300"
html = html.replace(old_card, new_card)

# 2. Refine save changes blue buttons
old_blue_btn_1 = "bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl shadow"
new_blue_btn_1 = "bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white px-8 py-3 rounded-2xl shadow-lg hover:shadow-indigo-500/25 hover:-translate-y-1 transition-all duration-300 font-semibold"
html = html.replace(old_blue_btn_1, new_blue_btn_1)

old_blue_btn_2 = "bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl"
html = html.replace(old_blue_btn_2, new_blue_btn_1)

# 3. Inputs
old_input = "mt-2 w-full border rounded-xl p-3"
new_input = "mt-2 w-full border border-slate-200 dark:border-slate-700 rounded-2xl p-4 bg-white/50 dark:bg-slate-950/50 focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 transition-all shadow-inner outline-none"
html = html.replace(old_input, new_input)

# Disable version input
old_disabled_input = "mt-2 w-full rounded-xl p-3 bg-slate-100 dark:bg-slate-800"
new_disabled_input = "mt-2 w-full border border-slate-200 dark:border-slate-700 rounded-2xl p-4 bg-slate-100/50 dark:bg-slate-800/50 shadow-inner cursor-not-allowed outline-none"
html = html.replace(old_disabled_input, new_disabled_input)

# 4. Regenerate Hero button (Green)
old_green_btn = "bg-green-600 hover:bg-green-700 text-white px-5 py-2 rounded-xl"
new_green_btn = "bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white px-6 py-2.5 rounded-2xl shadow-lg hover:shadow-teal-500/25 hover:-translate-y-0.5 transition-all duration-300 font-medium"
html = html.replace(old_green_btn, new_green_btn)

# 5. Regenerate Chapter (Purple)
old_purple_btn = "bg-purple-600 hover:bg-purple-700 text-white px-5 py-2 rounded-xl"
new_purple_btn = "bg-gradient-to-r from-fuchsia-600 to-purple-600 hover:from-fuchsia-700 hover:to-purple-700 text-white px-6 py-2.5 rounded-2xl shadow-lg hover:shadow-purple-500/25 hover:-translate-y-0.5 transition-all duration-300 font-medium"
html = html.replace(old_purple_btn, new_purple_btn)

# 6. Entire blog (Purple large)
old_purple_large = "bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-xl"
new_purple_large = "bg-gradient-to-r from-fuchsia-600 to-purple-600 hover:from-fuchsia-700 hover:to-purple-700 text-white px-8 py-3 rounded-2xl shadow-lg hover:shadow-purple-500/25 hover:-translate-y-1 transition-all duration-300 font-semibold flex items-center gap-2"
html = html.replace(old_purple_large, new_purple_large)

# 7. Paragraph blocks
old_p_block = "paragraph-block border rounded-xl p-5 mb-6"
new_p_block = "paragraph-block border border-slate-200/50 dark:border-slate-700/50 bg-slate-50/40 dark:bg-slate-800/40 rounded-2xl p-6 mb-8 hover:shadow-md transition-shadow"
html = html.replace(old_p_block, new_p_block)

# 8. Regenerate Paragraph (Blue small)
old_blue_small = "bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg"
new_blue_small = "bg-gradient-to-r from-blue-500 to-indigo-500 hover:from-blue-600 hover:to-indigo-600 text-white px-5 py-2 rounded-xl shadow-md hover:shadow-indigo-500/25 hover:-translate-y-0.5 transition-all duration-300 font-medium text-sm"
html = html.replace(old_blue_small, new_blue_small)

# 9. Paragraph textareas
old_p_textarea = "w-full border rounded-xl p-4"
new_p_textarea = "w-full border border-slate-200 dark:border-slate-700 rounded-2xl p-5 bg-white/50 dark:bg-slate-950/50 focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 transition-all shadow-inner outline-none leading-relaxed"
html = html.replace(old_p_textarea, new_p_textarea)

# 10. Modals
old_modal_card = "bg-white dark:bg-slate-900 rounded-2xl w-full max-w-3xl p-6"
new_modal_card = "bg-white/95 dark:bg-slate-900/95 backdrop-blur-2xl rounded-[2rem] w-full max-w-3xl p-8 shadow-2xl border border-white/20 dark:border-white/10"
html = html.replace(old_modal_card, new_modal_card)
html = html.replace("bg-white dark:bg-slate-900 rounded-2xl p-6 max-w-5xl", "bg-white/95 dark:bg-slate-900/95 backdrop-blur-2xl rounded-[2rem] p-8 max-w-5xl border border-white/20 dark:border-white/10 shadow-2xl")
html = html.replace("bg-white dark:bg-slate-900 rounded-2xl shadow-xl w-full max-w-5xl", "bg-white/95 dark:bg-slate-900/95 backdrop-blur-2xl rounded-[2rem] shadow-2xl w-full max-w-5xl border border-white/20 dark:border-white/10")

# 11. Modal buttons
html = html.replace("px-5 py-2 rounded-xl border", "px-6 py-2.5 rounded-2xl border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors font-medium")
html = html.replace("px-5 py-2 border rounded-xl", "px-6 py-2.5 rounded-2xl border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors font-medium")

# 12. Main title text
html = html.replace("text-4xl font-bold mt-3", "text-5xl font-extrabold mt-3 tracking-tight bg-gradient-to-r from-slate-900 to-slate-700 dark:from-white dark:to-slate-300 bg-clip-text text-transparent")

with open(target, 'w', encoding='utf-8') as f:
    f.write(html)

print("UI Refactoring Applied Successfully")
