import os

if __name__=="__main__":
    args = proc_opts()
    patreon = PatreonParser(args.download_dir)
    data = patreon.parse_patreon(args.infile)
    posts = patreon.parse_entries(data)
    patreon.persist_posts(posts, args.outfile)
    webbrowser.open_new_tab(patreon.next_page)

    if args.pages:
        for page in range(args.pages):
            print(f"On page {page}")
            posts = patreon.parse_entries(nxt)
            patreon.persist_posts(posts, args.outfile)
            nxt = patreon.get_next_entry()
