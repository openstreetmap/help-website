+++
type = "question"
title = "Can&#x27;t find configuration file of wireshark in Linux"
description = '''Hi, I installed wireshark in a remote server.But I am not able to see the wireshark folder inside /home/username/.config/ or in /etc/wireshark.conf .  I have access to remote server only through ssh. Actually I need to add some columns in preference file of wireshark.But I can&#x27;t see preference file ...'''
date = "2017-01-25T10:05:00Z"
lastmod = "2017-01-25T12:59:00Z"
weight = 59054
keywords = [ "configuration", "tshark", "columns", "server" ]
aliases = [ "/questions/59054" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can't find configuration file of wireshark in Linux](/questions/59054/cant-find-configuration-file-of-wireshark-in-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59054-score" class="post-score" title="current number of votes">0</div><span id="post-59054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I installed wireshark in a remote server.But I am not able to see the wireshark folder inside /home/username/.config/ or in /etc/wireshark.conf .</p><p>I have access to remote server only through ssh.</p><p>Actually I need to add some columns in preference file of wireshark.But I can't see preference file in any of these locations.</p><p>Right now I am doing the following method.But in the following code I need to add ip identification field(ip.id) also. Is there any method I can do it without adding a column in preference file.?</p><p>tshark -r capture.pcap -Y "udp or tcp and ip.dst == 192.22.167.00/24" -o "gui.column.format:\"Time\",\"%Yt\",\"Source address\",\"%s\",\"Protocol\",\"%p\",\"Destination address\",\"%d\",\"SrcPort\",\"%S\",\"DstPort\",\"%D\"" &gt; text</p><p>Server is using Ubuntu Zesty Zapus(17.04) and wireshark version is 2.2.4.</p><p>Thanks in advance</p><p>Subin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '17, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/95e9674b7a67d58ada813e0c6bc38d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subinjp&#39;s gravatar image" /><p><span>subinjp</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subinjp has no accepted answers">0%</span></p></div></div><div id="comments-container-59054" class="comments-container"></div><div id="comment-tools-59054" class="comment-tools"></div><div class="clear"></div><div id="comment-59054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59055"></span>

<div id="answer-container-59055" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59055-score" class="post-score" title="current number of votes">1</div><span id="post-59055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="subinjp has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Typically it's located in <code>$HOME/.wireshark/</code>, but if you want to add the <code>ip.id</code> field, you can do so with a custom column, such as <code>\"IP ID\",\"%Cus:ip.id:0:R\"</code> ... where the 0 indicates <strong>all</strong> occurrences of the field as opposed to only the 1st, 2nd, nth, or last occurrence, and the R indicates "Resolved", as opposed to "Unresolved", which typically makes more sense for things like addresses and ports.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '17, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jan '17, 10:55</strong> </span></p></div></div><div id="comments-container-59055" class="comments-container"><span id="59057"></span><div id="comment-59057" class="comment"><div id="post-59057-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for your response.It worked. Could you give a reference or a general pattern of adding custom columns in tshark.??</p></div><div id="comment-59057-info" class="comment-info"><span class="comment-age">(25 Jan '17, 10:37)</span> <span class="comment-user userinfo">subinjp</span></div></div><span id="59058"></span><div id="comment-59058" class="comment"><div id="post-59058-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, I don't think custom column formats are documented very well, at least not that I can find. Basically, the format is as I described though:</p><p><code>"Arbitrary Name","%Cus:fieldname"</code> ... with optional occurrence and resolved/unresolved flag. Use an occurrence value of -1 for the last occurrence, 0 for all occurrences and any other positive integer n for the nth occurrence. I'm not entirely sure, but resolved (R)/unresolved(U) may depend upon whether name resolution is enabled or not for those fields where it's applicable.</p></div><div id="comment-59058-info" class="comment-info"><span class="comment-age">(25 Jan '17, 11:00)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="59064"></span><div id="comment-59064" class="comment"><div id="post-59064-score" class="comment-score"></div><div class="comment-text"><p>Thank you.:)</p></div><div id="comment-59064-info" class="comment-info"><span class="comment-age">(25 Jan '17, 12:59)</span> <span class="comment-user userinfo">subinjp</span></div></div></div><div id="comment-tools-59055" class="comment-tools"></div><div class="clear"></div><div id="comment-59055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

