+++
type = "question"
title = "Error loading table &#x27;GeoIP Database Paths&#x27;: geoip_db_paths:5: unexpected char while looking for end of line"
description = '''Suddenly today I open wireshark and get this error.. Can i fix this. I dont need GeoIP datbase for my testing ..It is preventing the full loading of the pcap file. Error loading table &#x27;GeoIP Database Paths&#x27;: geoip_db_paths:5: unexpected char while looking for end of line Please help'''
date = "2013-10-07T09:36:00Z"
lastmod = "2013-10-08T08:08:00Z"
weight = 25718
keywords = [ "geoip", "errors" ]
aliases = [ "/questions/25718" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error loading table 'GeoIP Database Paths': geoip\_db\_paths:5: unexpected char while looking for end of line](/questions/25718/error-loading-table-geoip-database-paths-geoip_db_paths5-unexpected-char-while-looking-for-end-of-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25718-score" class="post-score" title="current number of votes">0</div><span id="post-25718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Suddenly today I open wireshark and get this error.. Can i fix this. I dont need GeoIP datbase for my testing ..It is preventing the full loading of the pcap file.</p><p>Error loading table 'GeoIP Database Paths': geoip_db_paths:5: unexpected char while looking for end of line</p><p>Please help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-geoip" rel="tag" title="see questions tagged &#39;geoip&#39;">geoip</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '13, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/581087043481fff131e3726feb3ce9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gederian&#39;s gravatar image" /><p><span>gederian</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gederian has no accepted answers">0%</span></p></div></div><div id="comments-container-25718" class="comments-container"></div><div id="comment-tools-25718" class="comment-tools"></div><div class="clear"></div><div id="comment-25718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25720"></span>

<div id="answer-container-25720" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25720-score" class="post-score" title="current number of votes">0</div><span id="post-25720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can simply rename or delete your <code>geoip_db_paths</code> file, but please share the contents of the file first if you plan on deleting it. It would be interesting to know what <em>unexpected char</em> was found that caused the problem.</p><p>The location of the <code>geoip_db_paths</code> file differs, depending on your platform, but the <a href="http://www.wireshark.org/docs/man-pages/wireshark.html">Wireshark man page</a> describes its location under the <strong>FILES</strong> section, but for the sake of convenience:</p><pre><code>The global preferences file is looked for in the wireshark directory under the share subdirectory of the main installation directory (for example, /usr/local/share/wireshark/preferences) on UNIX-compatible systems, and in the main installation directory (for example, C:\Program Files\Wireshark\preferences) on Windows systems.

The personal preferences file is looked for in $HOME/.wireshark/preferences on UNIX-compatible systems and %APPDATA%\Wireshark\preferences (or, if %APPDATA% isn&#39;t defined, %USERPROFILE%\Application Data\Wireshark\preferences) on Windows systems.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-25720" class="comments-container"><span id="25741"></span><div id="comment-25741" class="comment"><div id="post-25741-score" class="comment-score"></div><div class="comment-text"><p>The location of Wireshark dirs is also shown on the Folders tab of the "About Wireshark" dialog, and, on Windows at least, each location is a link that will open up Windows Explorer at the directory if double clicked.</p></div><div id="comment-25741-info" class="comment-info"><span class="comment-age">(08 Oct '13, 00:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="25745"></span><div id="comment-25745" class="comment"><div id="post-25745-score" class="comment-score"></div><div class="comment-text"><p>Yes, I should probably have mentioned that too, but I wasn't entirely sure what, "<em>It is preventing the full loading of the pcap file.</em>" meant, and in case it meant that it was causing Wireshark to crash, I wanted to provide a way to find the location of the file without having to actually launch Wireshark itself.</p><p>BTW, the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChUseHelpMenuSection.html">user guide</a> also mentions that the "About Wireshark" dialog indicates the used folders; however, it's probably not all that obvious:</p><p><strong>About Wireshark</strong></p><pre><code>This menu item brings up an information window that provides various detailed information items on Wireshark, such as how it&#39;s build, the plugins loaded, the used folders, ...</code></pre></div><div id="comment-25745-info" class="comment-info"><span class="comment-age">(08 Oct '13, 08:08)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-25720" class="comment-tools"></div><div class="clear"></div><div id="comment-25720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

