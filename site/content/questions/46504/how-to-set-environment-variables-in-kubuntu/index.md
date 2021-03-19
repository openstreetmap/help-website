+++
type = "question"
title = "how to set environment variables in kubuntu  ?"
description = '''Hello; How to set environment variables for wireshark in Kubuntu ? l have trouble when capturing an interface : there is no interface on wich a capture can be done Thank you for your help'''
date = "2015-10-13T11:09:00Z"
lastmod = "2015-10-13T14:47:00Z"
weight = 46504
keywords = [ "sniffing", "sniffer", "snifer", "network", "tcpip" ]
aliases = [ "/questions/46504" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to set environment variables in kubuntu ?](/questions/46504/how-to-set-environment-variables-in-kubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46504-score" class="post-score" title="current number of votes">0</div><span id="post-46504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello;</p><p>How to set environment variables for wireshark in Kubuntu ?</p><p>l have trouble when capturing an interface : there is no interface on wich a capture can be done</p><p>Thank you for your help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-sniffer" rel="tag" title="see questions tagged &#39;sniffer&#39;">sniffer</span> <span class="post-tag tag-link-snifer" rel="tag" title="see questions tagged &#39;snifer&#39;">snifer</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-tcpip" rel="tag" title="see questions tagged &#39;tcpip&#39;">tcpip</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '15, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/7b27a2956ad41514578aaf039fe4d7e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="agwmar&#39;s gravatar image" /><p><span>agwmar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="agwmar has no accepted answers">0%</span></p></div></div><div id="comments-container-46504" class="comments-container"></div><div id="comment-tools-46504" class="comment-tools"></div><div class="clear"></div><div id="comment-46504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46514"></span>

<div id="answer-container-46514" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46514-score" class="post-score" title="current number of votes">0</div><span id="post-46514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your problem is not related to 'environment variables'. It is (most certainly) related to access privileges.</p><p>Your need to run the command <strong>setcap</strong>. See my answers to similar questions:</p><blockquote><p><a href="https://ask.wireshark.org/questions/29555/no-interface-can-be-used">https://ask.wireshark.org/questions/29555/no-interface-can-be-used</a><br />
<a href="https://ask.wireshark.org/questions/19675/error-when-running-wireshark-on-ubuntu-as-non-root-user">https://ask.wireshark.org/questions/19675/error-when-running-wireshark-on-ubuntu-as-non-root-user</a><br />
</p></blockquote><p>and the wiki pages</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a><br />
<a href="http://wiki.wireshark.org/Development/PrivilegeSeparation">http://wiki.wireshark.org/Development/PrivilegeSeparation</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '15, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-46514" class="comments-container"><span id="46517"></span><div id="comment-46517" class="comment"><div id="post-46517-score" class="comment-score"></div><div class="comment-text"><p>when l set in my shell terminal this command : setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap it returns unable to set CAP_SETFCAP effective capability: Operation not permitted</p></div><div id="comment-46517-info" class="comment-info"><span class="comment-age">(13 Oct '15, 13:54)</span> <span class="comment-user userinfo">agwmar</span></div></div><span id="46519"></span><div id="comment-46519" class="comment"><div id="post-46519-score" class="comment-score"></div><div class="comment-text"><p>please run:</p><p><strong>sudo</strong> setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap</p></div><div id="comment-46519-info" class="comment-info"><span class="comment-age">(13 Oct '15, 13:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46522"></span><div id="comment-46522" class="comment"><div id="post-46522-score" class="comment-score"></div><div class="comment-text"><p>this command work but this one : chgrp wireshark /usr/bin/dumpcap</p><p>returns chgrp: invalid group: ‘wireshark’</p></div><div id="comment-46522-info" class="comment-info"><span class="comment-age">(13 Oct '15, 14:06)</span> <span class="comment-user userinfo">agwmar</span></div></div><span id="46525"></span><div id="comment-46525" class="comment"><div id="post-46525-score" class="comment-score"></div><div class="comment-text"><p>please read the wiki links I posted and the docs of your OS!</p><blockquote><p><a href="http://manpages.ubuntu.com/manpages/trusty/man8/adduser.8.html">http://manpages.ubuntu.com/manpages/trusty/man8/adduser.8.html</a><br />
<a href="http://askubuntu.com/questions/66718/how-to-manage-users-and-groups">http://askubuntu.com/questions/66718/how-to-manage-users-and-groups</a></p></blockquote></div><div id="comment-46525-info" class="comment-info"><span class="comment-age">(13 Oct '15, 14:45)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46526"></span><div id="comment-46526" class="comment"><div id="post-46526-score" class="comment-score"></div><div class="comment-text"><p>sudo addgroup wireshark<br />
sudo usermod -a -G wireshark YOUR_USER_NAME<br />
sudo chown root:wireshark /usr/bin/dumpcap<br />
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap</p></div><div id="comment-46526-info" class="comment-info"><span class="comment-age">(13 Oct '15, 14:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46514" class="comment-tools"></div><div class="clear"></div><div id="comment-46514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

