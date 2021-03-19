+++
type = "question"
title = "Tshark revolving file collection"
description = '''I am interested in running a startup script in windows that runs tshark.exe -i 1 -a filesize:100000 -b files:10 -w revolvingfiles  The idea is to only have a maximum of 1GB of harddrive space occupied at any given time, but to have the collection start at boot up. The problem is that when you re-run...'''
date = "2015-07-07T09:58:00Z"
lastmod = "2015-07-09T08:55:00Z"
weight = 43936
keywords = [ "windows", "revolving", "startup", "tshark" ]
aliases = [ "/questions/43936" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark revolving file collection](/questions/43936/tshark-revolving-file-collection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43936-score" class="post-score" title="current number of votes">0</div><span id="post-43936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am interested in running a startup script in windows that runs <em>tshark.exe -i 1 -a filesize:100000 -b files:10 -w revolvingfiles</em></p><p>The idea is to only have a maximum of 1GB of harddrive space occupied at any given time, but to have the collection start at boot up. The problem is that when you re-run the command above it finds the next available number and starts its count over. This would would occupy 3GB of space after being run three times.</p><p>Is there a way to force tshark to recognize the existence of previous files and to maintain the state of 10 files after multiple executions of the program (ie. after 3 reboots, still having only 10 files)</p><p>I understand that I could write a script that deletes the previous set of files, but this is not ideal.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-revolving" rel="tag" title="see questions tagged &#39;revolving&#39;">revolving</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '15, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/0a92214fd94d818059f740cdd56be7af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="greenfreq&#39;s gravatar image" /><p><span>greenfreq</span><br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="greenfreq has one accepted answer">33%</span></p></div></div><div id="comments-container-43936" class="comments-container"></div><div id="comment-tools-43936" class="comment-tools"></div><div class="clear"></div><div id="comment-43936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43944"></span>

<div id="answer-container-43944" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43944-score" class="post-score" title="current number of votes">1</div><span id="post-43944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="greenfreq has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have a script (batch file) that basically does this. Here's the basic usage:</p><p><code></code></p><code></code><pre><code>A batch file that allows you to limit the number of files in a directory or
the total disk space consumed by those files, or both.  Optionally, you can
specify a particular file pattern to match rather than the default, which is
for all files.

WARNING: All files in excess of the maximum allowed WILL BE DELETED!

Usage: maxfiles.bat &lt;-d dir&gt; [options] ... where options are:

[-c countlimit] [-s sizelimit] [-p pattern] [-r secs] [-q] [-h]

-d dir        The directory of files. (Required!)
-c countlimit The maximum number of files allowed in the directory.
-s sizelimit  The maximum size limit of the files in the directory.
-p pattern    The file matching pattern. (Default is all files)
-r secs       Run continuously with a specified delay between loops.
-q            Run quietly.
-h            Display this help and exit.</code></pre></code><p><code></code></p><p><em>Disclaimer</em>: It hasn't seen a lot of testing since I just wrote it today, and it has problems with file names that contain certain rather problematic characters in them, but if you avoid naming your files with characters such as <code>"@#$%&amp; ()_+{}~-=[];'</code> then it <strong>should</strong> be OK. (Some of those characters are actually not a problem, but I forget exactly which ones.)</p><p>You indicated that, <em>"but this is not ideal."</em>, so maybe this is of no use to you? Anyway, let me know if you're interested. I'm not quite sure where I'd post it though, but we'll figure something out, I guess.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '15, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-43944" class="comments-container"><span id="43945"></span><div id="comment-43945" class="comment"><div id="post-43945-score" class="comment-score"></div><div class="comment-text"><p>In case it's not obvious, the files that get deleted are the <em>oldest</em> ones in excess of the maximum allowable thresholds set by the caller.</p></div><div id="comment-43945-info" class="comment-info"><span class="comment-age">(07 Jul '15, 15:05)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="43948"></span><div id="comment-43948" class="comment"><div id="post-43948-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the reply, and the offer for the script. In most cases you can post scripts to websites like <a href="http://pastebin.com/">http://pastebin.com/</a> which will give you a link that points to the code you pasted.</p><p>I would be interested in seeing how the script performs.</p></div><div id="comment-43948-info" class="comment-info"><span class="comment-age">(07 Jul '15, 15:50)</span> <span class="comment-user userinfo">greenfreq</span></div></div><span id="43949"></span><div id="comment-43949" class="comment"><div id="post-43949-score" class="comment-score"></div><div class="comment-text"><p>For now, I posted the batch file at <a href="https://wiki.wireshark.org/Tools">https://wiki.wireshark.org/Tools</a>. I found one bug after posting it, so the file there now is the updated one with md5sum = c8984274e92ffa1f09c108471113fed1.</p><p>Example usage:</p><pre><code>maxfiles.bat -d C:\path\to\captures -c 10 -p *.pcap* -q</code></pre><p>I've tested it, but please use with caution since it will delete files! You can report any bugs you find and I'll try to fix them ... or you can feel free to fix them yourself. :)</p></div><div id="comment-43949-info" class="comment-info"><span class="comment-age">(07 Jul '15, 18:19)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="43950"></span><div id="comment-43950" class="comment"><div id="post-43950-score" class="comment-score"></div><div class="comment-text"><p>The potential "problematic characters" I mentioned earlier actually seem all OK to use except for one - the space character, so at least for now, avoid using spaces in your capture file names if you plan to use the batch file.</p></div><div id="comment-43950-info" class="comment-info"><span class="comment-age">(07 Jul '15, 18:46)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="43951"></span><div id="comment-43951" class="comment not_top_scorer"><div id="post-43951-score" class="comment-score"></div><div class="comment-text"><p>OK, the problem with spaces in the filename should be fixed now. The current md5sum(maxfiles.bat) = 3609ff3a171da4910e2ccaf42ec5f716.</p></div><div id="comment-43951-info" class="comment-info"><span class="comment-age">(07 Jul '15, 19:26)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="43952"></span><div id="comment-43952" class="comment not_top_scorer"><div id="post-43952-score" class="comment-score"></div><div class="comment-text"><p>OK, I've forgotten how much I hate working with batch files. I made one more tweak so I updated it once again and the latest md5sum(maxfiles.bat) = 9d7e39d8cd8454a19bde900840d93ebd.</p></div><div id="comment-43952-info" class="comment-info"><span class="comment-age">(07 Jul '15, 19:37)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="43974"></span><div id="comment-43974" class="comment not_top_scorer"><div id="post-43974-score" class="comment-score"></div><div class="comment-text"><p>Ok, so to make sure I understand the batch file. It does not execute tshark, but is designed to run in tandem with it, checking periodically to see if the maximum number of files, or maximum size used has been exceeded and then deleting, starting with the oldest file, all files necessary to meet the specific number or size limits. Also, what is the unit of measure for -s?</p></div><div id="comment-43974-info" class="comment-info"><span class="comment-age">(08 Jul '15, 10:06)</span> <span class="comment-user userinfo">greenfreq</span></div></div><span id="43977"></span><div id="comment-43977" class="comment not_top_scorer"><div id="post-43977-score" class="comment-score"></div><div class="comment-text"><p>Correct. It knows nothing about <code>tshark</code> (or <code>dumpcap</code> or anything else for that matter). It only concerns itself with the files, regardless of what program(s) were used to generate those files.</p><p>It could be run once at startup to prune files in a given directory and then terminate, or it could be started so that it continues to monitor the directory by using the <code>-r secs</code> option.</p><p>Currently, <code>-s</code> is in units of bytes. I know it's not necessarily the most convenient unit and I considered using another unit (or allowing other units), but I did not implement that yesterday. Consider that, "an exercise for the reader". :)</p></div><div id="comment-43977-info" class="comment-info"><span class="comment-age">(08 Jul '15, 11:00)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="44014"></span><div id="comment-44014" class="comment"><div id="post-44014-score" class="comment-score">1</div><div class="comment-text"><p>I will mark your sccript as an accepted answer as I was able to set up a start up for both it and my tshark script and so now tshark rotates on 10 files and your script clears out anything over 15 files at 30 minute intervals. Thanks again.</p></div><div id="comment-44014-info" class="comment-info"><span class="comment-age">(09 Jul '15, 08:41)</span> <span class="comment-user userinfo">greenfreq</span></div></div><span id="44016"></span><div id="comment-44016" class="comment not_top_scorer"><div id="post-44016-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the feedback. I'm glad the batch file was useful to you.</p></div><div id="comment-44016-info" class="comment-info"><span class="comment-age">(09 Jul '15, 08:55)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-43944" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-43944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

