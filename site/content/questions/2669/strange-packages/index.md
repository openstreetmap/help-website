+++
type = "question"
title = "strange packages"
description = '''Hello! My computer sends packets that look as: http://img339.imageshack.us/i/screenkx.png/ these packages can be several hundred. What are these strange packages?'''
date = "2011-03-04T13:59:00Z"
lastmod = "2011-03-07T07:40:00Z"
weight = 2669
keywords = [ "strange", "packages" ]
aliases = [ "/questions/2669" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [strange packages](/questions/2669/strange-packages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2669-score" class="post-score" title="current number of votes">0</div><span id="post-2669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! My computer sends packets that look as:</p><p><a href="http://img339.imageshack.us/i/screenkx.png/">http://img339.imageshack.us/i/screenkx.png/</a></p><p>these packages can be several hundred. What are these strange packages?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-strange" rel="tag" title="see questions tagged &#39;strange&#39;">strange</span> <span class="post-tag tag-link-packages" rel="tag" title="see questions tagged &#39;packages&#39;">packages</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '11, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/6ba80460a5a019d83c9440e96642d127?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blitzer&#39;s gravatar image" /><p><span>blitzer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blitzer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Mar '11, 23:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-2669" class="comments-container"></div><div id="comment-tools-2669" class="comment-tools"></div><div class="clear"></div><div id="comment-2669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2690"></span>

<div id="answer-container-2690" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2690-score" class="post-score" title="current number of votes">2</div><span id="post-2690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A great screenshot! You did a good job in linking the HTTP request to the flood of UDP packets.</p><p>It looks like someone uploaded a PHP script called "..php" into the webservers webdav directory. From the looks of the screenshot the script is used to direct a DoS attack to a victim IP address.</p><p>While UDP packets occasionally get fragmented this excessive flood of packets is certainly malicious.</p><p>Here a couple of ideas for follow ups:</p><ul><li>Harden your web server</li><li>Remove the malicious scripts from the server (you might want to reinstall the whole box)</li><li>Establish firewall rules that limit outgoing traffic. In my opinion a webserver does not need full outgoing web access</li></ul><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '11, 00:58</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-2690" class="comments-container"><span id="2678"></span><div id="comment-2678" class="comment"><div id="post-2678-score" class="comment-score"></div><div class="comment-text"><p>That is strange. What is the highest level protocol seen?</p></div><div id="comment-2678-info" class="comment-info"><span class="comment-age">(05 Mar '11, 16:35)</span> <span class="comment-user userinfo">Paul Stewart</span></div></div><span id="2687"></span><div id="comment-2687" class="comment"><div id="post-2687-score" class="comment-score"></div><div class="comment-text"><p><a href="http://img189.imageshack.us/i/wiresharkw.png/">http://img189.imageshack.us/i/wiresharkw.png/</a></p><p>It lasted a minute. 775961 packets sent in a minute!? DoS attack? The processes created by Apache.</p><p>Sorry for my English. I use google translator;)</p><p><a href="http://img153.imageshack.us/i/wireshark2.png/">http://img153.imageshack.us/i/wireshark2.png/</a></p><p>This ip: 85.17.159.77 twice already today started sending packages</p></div><div id="comment-2687-info" class="comment-info"><span class="comment-age">(06 Mar '11, 22:25)</span> <span class="comment-user userinfo">blitzer</span></div></div><span id="2691"></span><div id="comment-2691" class="comment"><div id="post-2691-score" class="comment-score"></div><div class="comment-text"><p>Yarp - google'ing for "GET /webdav/..php?act=phptools" links to several haXXing sites - doesn't look too good - although a huge number of "x" bytes doesn't make up usable shellcode... but maybe there is one in later packets...</p></div><div id="comment-2691-info" class="comment-info"><span class="comment-age">(07 Mar '11, 01:56)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="2693"></span><div id="comment-2693" class="comment"><div id="post-2693-score" class="comment-score"></div><div class="comment-text"><blockquote><p>You did a good job in linking the HTTP request to the flood of UDP packets</p></blockquote><p>I did not do anything ;)</p><p>/webdav/..php?.......... directory in screenshot it is about my www directory?</p></div><div id="comment-2693-info" class="comment-info"><span class="comment-age">(07 Mar '11, 02:18)</span> <span class="comment-user userinfo">blitzer</span></div></div><span id="2698"></span><div id="comment-2698" class="comment"><div id="post-2698-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.apachefriends.org/f/viewtopic.php?f=16&amp;t=44140">http://www.apachefriends.org/f/viewtopic.php?f=16&amp;t=44140</a></p><p>This is a description of my problem. In webdav folder I found strange files. Apache logs show that the files were uploaded on March 3. On this day, began to have problems. I used the solution shown above link. See if help;)</p></div><div id="comment-2698-info" class="comment-info"><span class="comment-age">(07 Mar '11, 07:40)</span> <span class="comment-user userinfo">blitzer</span></div></div></div><div id="comment-tools-2690" class="comment-tools"></div><div class="clear"></div><div id="comment-2690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

