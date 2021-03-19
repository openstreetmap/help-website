+++
type = "question"
title = "Permission denied while running wireshark"
description = '''I had a wireshark distribution with me. It is on linux and works well. Now I have to put this wireshark binary on a server. So I used ftp to get the wireshark directory on my server. I copied it in the /root folder.  wireshark has root:root onwership and drwxr-xr-x permissions. When I go the wiresha...'''
date = "2011-06-03T05:20:00Z"
lastmod = "2011-06-03T05:23:00Z"
weight = 4363
keywords = [ "permission", "wireshark" ]
aliases = [ "/questions/4363" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Permission denied while running wireshark](/questions/4363/permission-denied-while-running-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4363-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I had a wireshark distribution with me. It is on linux and works well. Now I have to put this wireshark binary on a server. So I used ftp to get the wireshark directory on my server. I copied it in the /root folder.</p><p>wireshark has root:root onwership and drwxr-xr-x permissions.</p><p>When I go the wireshark directory and try to run wireshark using ./wireshark I get this error ---</p><p><strong>-bash: ./wireshark: Permission denied</strong></p></div><div id="question-tags" class="tags-container tags">permission wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '11, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jun '11, 07:41</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4363" class="comments-container"><span id="4370"></span><div id="comment-4370" class="comment"><div id="post-4370-score" class="comment-score">1</div><div class="comment-text"><p>Anything where ls reports "drwxr-xr-x permissions" is a directory - the "d" isn't a permission, it's a file type. What are the permissions on the <em>file</em> named "wireshark" - i.e., when you go to the wireshark directory and type "ls -l ./wireshark", what does it print?</p></div><div id="comment-4370-info" class="comment-info"><span class="comment-age">(03 Jun '11, 20:02)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-4363" class="comment-tools"></div><div class="clear"></div><div id="comment-4363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4364"></span>

<div id="answer-container-4364" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4364-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>try using sudo wireshark or sudo tshark also.. you can try gksu wireshark or gksu tshark</p><p>hope this helps, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '11, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-4364" class="comments-container"><span id="4365"></span><div id="comment-4365" class="comment"><div id="post-4365-score" class="comment-score"></div><div class="comment-text"><p>Hello John,</p><p>When I do a sudo wireshark, this is what I get --&gt;&gt;</p><p>sudo: wireshark: command not found</p></div><div id="comment-4365-info" class="comment-info"><span class="comment-age">(03 Jun '11, 06:20)</span> sid</div></div><span id="4366"></span><div id="comment-4366" class="comment"><div id="post-4366-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure which version of Linux you're running, but you might try the linux distributable from wireshark.org. http://www.wireshark.org/download.html On the bottom right there will be downloadable distributions based on the version of Linux you're running. I'm running it on a few Linux boxes, but they're both Debian, so I'm not sure about the other versions. sudo will run wireshark with supervisor/admin priveleges, but if it doesn't find Wireshark or Tshark applications, you'll get the error you showed above. gksu will also allow you to run the applications with supervisory priveleges. So those 2 commands will help get around a possible security/access problem. I used the Synaptic Package Manager to install Wireshark under Linux.</p><p>Sorry that didn't work for you, John</p></div><div id="comment-4366-info" class="comment-info"><span class="comment-age">(03 Jun '11, 07:00)</span> John_Modlin</div></div><span id="4376"></span><div id="comment-4376" class="comment"><div id="post-4376-score" class="comment-score">2</div><div class="comment-text"><p>Make sure you run <code>sudo ./wireshark</code> (and not <code>sudo wireshark</code> unless <code>wireshark</code> is in your path, which doesn't appear to be the case).</p></div><div id="comment-4376-info" class="comment-info"><span class="comment-age">(04 Jun '11, 17:11)</span> helloworld</div></div></div><div id="comment-tools-4364" class="comment-tools"></div><div class="clear"></div><div id="comment-4364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

