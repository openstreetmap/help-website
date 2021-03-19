+++
type = "question"
title = "how do I rename wireshark files in second folder to same name as files in old folder"
description = '''Hi, I currently have two folders, one with WireShark .pcapng files(folder A) and one with .csv files(folder B) that correspond with the .pcapng files. I would like to know if there is any way I can rename the files in folder B to have the same name as the files in folder A? i&#x27;ve tried the replace co...'''
date = "2012-08-28T06:06:00Z"
lastmod = "2012-08-28T21:31:00Z"
weight = 13932
keywords = [ "conversion", "code", "wireshark" ]
aliases = [ "/questions/13932" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how do I rename wireshark files in second folder to same name as files in old folder](/questions/13932/how-do-i-rename-wireshark-files-in-second-folder-to-same-name-as-files-in-old-folder)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13932-score" class="post-score" title="current number of votes">0</div><span id="post-13932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I currently have two folders, one with WireShark .pcapng files(folder A) and one with .csv files(folder B) that correspond with the .pcapng files. I would like to know if there is any way I can rename the files in folder B to have the same name as the files in folder A?</p><p>i've tried the replace command but couldn’t manipulate it to do what I want . Is there any way this is possible? Thanks, Jennifer</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span> <span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '12, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/04f74668a166a2e978a7a929d98a29c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="7878987&#39;s gravatar image" /><p><span>7878987</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="7878987 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Aug '12, 08:45</strong> </span></p></div></div><div id="comments-container-13932" class="comments-container"></div><div id="comment-tools-13932" class="comment-tools"></div><div class="clear"></div><div id="comment-13932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13935"></span>

<div id="answer-container-13935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13935-score" class="post-score" title="current number of votes">0</div><span id="post-13935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you can rename files on Windows with the ren (rename) command, and on Linux/Unix you can use the mv (move) command. As in "ren file1.pcapng fileA.pcapng" or "mv file1.pcapng fileA.pcapng". Note that it's dangerous to change the filename suffix (.pcapng) to something else, since it will not change the internal format of the files, and will tend to be confusing. Wireshark will still process the files, regardless of the suffix, if opened directly with Wireshark, but it's still confusing and not recommended.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '12, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p><span>griff</span><br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span></p></div></div><div id="comments-container-13935" class="comments-container"><span id="13937"></span><div id="comment-13937" class="comment"><div id="post-13937-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I have converted the files using tshark and extracted specific information into an excel file.What im having problems with keeping the same name for the excel files as the wireshark capture files.I might need to use a string so im currently experimenting with that.</p><p>Thanks,</p></div><div id="comment-13937-info" class="comment-info"><span class="comment-age">(28 Aug '12, 08:42)</span> <span class="comment-user userinfo">7878987</span></div></div><span id="13949"></span><div id="comment-13949" class="comment"><div id="post-13949-score" class="comment-score"></div><div class="comment-text"><p>You do not want Wireshark files and Excel CSV files to have the <em>exact</em> same name, as the former files should be called {something}.pcapng and the latter files should be called {something}.csv. Pcap-ng files should <em>not</em> be given the suffix ".csv" and CSV files for Excel should <em>not</em> be given the suffix ".pcapng", for the reasons griff gave.</p><p>If you want to have the CSV file produced from foobar.pcapng to be named foobar.csv, and that's not the case with the files in folders A and B, you might have to rename them one at a time by hand.</p></div><div id="comment-13949-info" class="comment-info"><span class="comment-age">(28 Aug '12, 21:31)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-13935" class="comment-tools"></div><div class="clear"></div><div id="comment-13935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13940"></span>

<div id="answer-container-13940" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13940-score" class="post-score" title="current number of votes">0</div><span id="post-13940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Why do you want to rename the files? If the CSV files were generated with tshark (or wireshark), simply repeat the "export" operation and this time use the correct filename ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '12, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13940" class="comments-container"></div><div id="comment-tools-13940" class="comment-tools"></div><div class="clear"></div><div id="comment-13940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

