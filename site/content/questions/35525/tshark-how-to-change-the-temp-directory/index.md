+++
type = "question"
title = "tshark - how to change the temp directory"
description = '''Hello I have tshark running on a windows 2012 server, and it is writing its temp files to this directory. C:&#92;Users&#92;%Username%&#92;AppData&#92;Local&#92;Temp I need to move it to a new disk and directory  d:&#92;Temp I have changed the TEMP,TMP,TMPDIR environment variables to the new path D:&#92;Temp and when I go to wi...'''
date = "2014-08-18T02:17:00Z"
lastmod = "2014-08-18T04:54:00Z"
weight = 35525
keywords = [ "tshark", "temp" ]
aliases = [ "/questions/35525" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark - how to change the temp directory](/questions/35525/tshark-how-to-change-the-temp-directory)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35525-score" class="post-score" title="current number of votes">0</div><span id="post-35525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I have tshark running on a windows 2012 server, and it is writing its temp files to this directory. C:\Users\%Username%\AppData\Local\Temp I need to move it to a new disk and directory d:\Temp I have changed the TEMP,TMP,TMPDIR environment variables to the new path D:\Temp and when I go to wireshark -&gt; abut -&gt; folders I can see the D:\Temp however the tshark keeps writing its temp files to the drive C: location. how can i make tshark write to the new directory. thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-temp" rel="tag" title="see questions tagged &#39;temp&#39;">temp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '14, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/cb9768792db4fe8dfecf910a439177ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="avi_m1968&#39;s gravatar image" /><p><span>avi_m1968</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="avi_m1968 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Aug '14, 02:35</strong> </span></p></div></div><div id="comments-container-35525" class="comments-container"></div><div id="comment-tools-35525" class="comment-tools"></div><div class="clear"></div><div id="comment-35525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35526"></span>

<div id="answer-container-35526" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35526-score" class="post-score" title="current number of votes">1</div><span id="post-35526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TShark/dumpcap uses the TEMP directory from the <strong>user</strong> environment variables - have you changed that one, or the system one? You could also always force tshark/dumpcap to write files to a specific location by using the "-w" parameter.</p><p>You might also be interested in this blog post: <a href="http://blog.packet-foo.com/2014/07/wireshark-file-storage/">http://blog.packet-foo.com/2014/07/wireshark-file-storage/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '14, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35526" class="comments-container"><span id="35527"></span><div id="comment-35527" class="comment"><div id="post-35527-score" class="comment-score"></div><div class="comment-text"><p>Hello I have changed the USER ENV not the system. I can't use the -w since I'm reading the STDOUT of tshark if I use it I don't see STDOUT. any idea's what I'm doing wrong? thank you</p></div><div id="comment-35527-info" class="comment-info"><span class="comment-age">(18 Aug '14, 02:40)</span> <span class="comment-user userinfo">avi_m1968</span></div></div><span id="35528"></span><div id="comment-35528" class="comment"><div id="post-35528-score" class="comment-score"></div><div class="comment-text"><p>Have you verified that the command session you're running tshark in actually has the TEMP setting you assume? I usually check this by running the "SET" command. Maybe you're running the command line as a different user, e.g. from a task scheduler account?</p></div><div id="comment-35528-info" class="comment-info"><span class="comment-age">(18 Aug '14, 02:42)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="35529"></span><div id="comment-35529" class="comment"><div id="post-35529-score" class="comment-score"></div><div class="comment-text"><p>I'm running the script from the task scheduler, but it is running as the user that i changed in his profile the environment variables. I have added commands to the script that would check and write to the file the environment variables that the script see's and i'll update you.</p></div><div id="comment-35529-info" class="comment-info"><span class="comment-age">(18 Aug '14, 04:19)</span> <span class="comment-user userinfo">avi_m1968</span></div></div><span id="35532"></span><div id="comment-35532" class="comment"><div id="post-35532-score" class="comment-score">1</div><div class="comment-text"><p>you are right, even that the user ENV vars were changed when running the script it used the global ENV setting I added the the 3 SET commands TEMP,TMP,TMPDIR to the script before running tshark and it solved the problem. thank you :-)</p></div><div id="comment-35532-info" class="comment-info"><span class="comment-age">(18 Aug '14, 04:54)</span> <span class="comment-user userinfo">avi_m1968</span></div></div></div><div id="comment-tools-35526" class="comment-tools"></div><div class="clear"></div><div id="comment-35526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

