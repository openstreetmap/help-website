+++
type = "question"
title = "Want to insert comment in wireshark capture file."
description = '''I&#x27;m relatively new to wireshark. I&#x27;m using an older Fedora wireshark-gnome for some debugging and testing of another system. I would like to be able to insert a comment or text note into the capture file before performing an action on the system being tested (where wireshark will capture the results...'''
date = "2013-03-08T09:46:00Z"
lastmod = "2015-06-23T17:56:00Z"
weight = 19303
keywords = [ "wireshard", "add_note", "gnome" ]
aliases = [ "/questions/19303" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Want to insert comment in wireshark capture file.](/questions/19303/want-to-insert-comment-in-wireshark-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19303-score" class="post-score" title="current number of votes">0</div><span id="post-19303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm relatively new to wireshark. I'm using an older Fedora wireshark-gnome for some debugging and testing of another system. I would like to be able to insert a comment or text note into the capture file before performing an action on the system being tested (where wireshark will capture the results). I did not see anything like this is in the GUI. <strong>Am I missing something?</strong></p><p>Regards, Chad Farmer</p><p>I understand the complexity of inserting data at arbirtary points within a capture file while it is being recorded, so I would be happy to just insert a comment into the capture file "stream".</p><p>A more complex design would be to have an external file of comments indexed to a capture file(s) and with the display and editing of comments integrated into the GUI. Unfortunately, I'm not interested in implementing it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshard" rel="tag" title="see questions tagged &#39;wireshard&#39;">wireshard</span> <span class="post-tag tag-link-add_note" rel="tag" title="see questions tagged &#39;add_note&#39;">add_note</span> <span class="post-tag tag-link-gnome" rel="tag" title="see questions tagged &#39;gnome&#39;">gnome</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '13, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/3c7618d31ed754f5a8acab1f1f1a32e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chad%20Farmer&#39;s gravatar image" /><p><span>Chad Farmer</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chad Farmer has no accepted answers">0%</span></p></div></div><div id="comments-container-19303" class="comments-container"></div><div id="comment-tools-19303" class="comment-tools"></div><div class="clear"></div><div id="comment-19303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19304"></span>

<div id="answer-container-19304" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19304-score" class="post-score" title="current number of votes">2</div><span id="post-19304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to move to Wireshark 1.8.x or later as that supports pcapng, a new capture file format that allows comments (or annotations) to be added. The Wireshark UI allows you to view and edit the comments.</p><p>See the <a href="https://blog.wireshark.org/2012/03/wireshark-and-pcap-ng/">blog post</a> from <span>@Gerald</span>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '13, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Mar '13, 09:52</strong> </span></p></div></div><div id="comments-container-19304" class="comments-container"><span id="19312"></span><div id="comment-19312" class="comment"><div id="post-19312-score" class="comment-score">1</div><div class="comment-text"><p>Thank you. It seemed like too useful of an idea to not exist.</p></div><div id="comment-19312-info" class="comment-info"><span class="comment-age">(08 Mar '13, 12:09)</span> <span class="comment-user userinfo">Chad Farmer</span></div></div><span id="43489"></span><div id="comment-43489" class="comment"><div id="post-43489-score" class="comment-score"></div><div class="comment-text"><p>Agreed. (Feature is "Too useful to not exist") Thanks for the link to blog post on the differences between pcap and pcap-ng formats. Came here with the same question as the original poster. First time I've stumbled on a reason to prefer the new format.</p><p>Apart from, "Well it says NG". : )</p></div><div id="comment-43489-info" class="comment-info"><span class="comment-age">(23 Jun '15, 17:56)</span> <span class="comment-user userinfo">sir-isaac-ha...</span></div></div></div><div id="comment-tools-19304" class="comment-tools"></div><div class="clear"></div><div id="comment-19304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

