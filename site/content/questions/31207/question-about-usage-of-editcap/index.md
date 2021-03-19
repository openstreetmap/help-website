+++
type = "question"
title = "question about usage of editcap"
description = '''Hi all,  I&#x27;m very beginner with wireshark and posting to know how can i use editcap.  refer to the below   abc.pcap is present under /Program Files/Wireshark/ and hope to create another output file(123.pcap) with count=100 but editcap shows &quot;Permission denied&quot; on my console(windows 7)  how can i fix...'''
date = "2014-03-26T21:35:00Z"
lastmod = "2014-03-27T02:38:00Z"
weight = 31207
keywords = [ "editcap" ]
aliases = [ "/questions/31207" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [question about usage of editcap](/questions/31207/question-about-usage-of-editcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31207-score" class="post-score" title="current number of votes">0</div><span id="post-31207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm very beginner with wireshark and posting to know how can i use editcap. refer to the below</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ScreenHunter_01_Mar._27_13.26_1.jpg" alt="alt text" /></p><p>abc.pcap is present under /Program Files/Wireshark/ and hope to create another output file(123.pcap) with count=100 but editcap shows "Permission denied" on my console(windows 7) how can i fix it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '14, 21:35</strong></p><img src="https://secure.gravatar.com/avatar/27e4d1e97303115b07caf9ba39267f2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ray_Han&#39;s gravatar image" /><p><span>Ray_Han</span><br />
<span class="score" title="56 reputation points">56</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ray_Han has no accepted answers">0%</span></p></img></div></div><div id="comments-container-31207" class="comments-container"></div><div id="comment-tools-31207" class="comment-tools"></div><div class="clear"></div><div id="comment-31207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31208"></span>

<div id="answer-container-31208" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31208-score" class="post-score" title="current number of votes">1</div><span id="post-31208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ray_Han has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is you're trying to create this <code>123.pcap</code> file in a directory you don't have permissions to create files in, or there's an existing file of that name you don't have permissions to overwrite. Try running <code>editcap</code> from a different directory so the file gets created in a directory you have permissions for, or put a path to such a directory in front of the <code>123.pcap</code> filename.</p><p>Like try this:</p><pre><code>editcap -r abc.pcap ..\123.pcap 100</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '14, 21:58</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-31208" class="comments-container"><span id="31210"></span><div id="comment-31210" class="comment"><div id="post-31210-score" class="comment-score"></div><div class="comment-text"><p>Hi I have resolved it i executed command prompt(CMD) with non-administrator account(just user account). after executing it with administrator account, it works well. Thanks</p></div><div id="comment-31210-info" class="comment-info"><span class="comment-age">(26 Mar '14, 23:54)</span> <span class="comment-user userinfo">Ray_Han</span></div></div></div><div id="comment-tools-31208" class="comment-tools"></div><div class="clear"></div><div id="comment-31208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31213"></span>

<div id="answer-container-31213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31213-score" class="post-score" title="current number of votes">1</div><span id="post-31213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As per the answer from <span>@Hadriel</span>, this is a permissions problem in that a normal cmd prompt doesn't have write access to the <code>Program Files</code> directory, but an elevated cmd prompt does. However the reason for this restriction is that it's generally not a good idea as:</p><ol><li>Inadvertent writes to the directory could break something.</li><li>Running Wireshark suite components with administrator privileges might be a security risk.</li></ol><p>Changing to a directory that does allow you to write to it, e.g. the users <code>Documents</code>, then brings the issue that the Wireshark binaries are not on the path, so you must either specify the full path on the command line, i.e. in your case <code>"C:\Program Files\Wireshark\editcap.exe"</code>, using the quotes because the path is a space in it, or add the <code>C:\Program Files\Wireshark</code> directory to the path either temporarily for the cmd prompt session using <code>set PATH=%PATH%;C:\Program Files\Wireshark</code> or more permanently using the "Environment Variables" dialog from the "System Properties" dialog to set the user or system PATH to include the Wireshark directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-31213" class="comments-container"></div><div id="comment-tools-31213" class="comment-tools"></div><div class="clear"></div><div id="comment-31213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

