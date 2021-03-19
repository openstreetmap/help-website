+++
type = "question"
title = "My network traffic looks exactly like the dns-remoteshell.pcap. What now???"
description = '''Okay, so I am having problems with a Fedora Core 14 Linux machine. I inherited it recently from my late brother and while he was a Linux GOD, I am merely a mortal. I know something, somewhat about Linux from my days as a contributing editor at Newsforge (talk about embarrassing, asking this when I u...'''
date = "2011-08-10T06:39:00Z"
lastmod = "2011-08-10T11:25:00Z"
weight = 5620
keywords = [ "virus", "remoteshell", "worm", "dns" ]
aliases = [ "/questions/5620" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [My network traffic looks exactly like the dns-remoteshell.pcap. What now???](/questions/5620/my-network-traffic-looks-exactly-like-the-dns-remoteshellpcap-what-now)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5620-score" class="post-score" title="current number of votes">0</div><span id="post-5620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Okay, so I am having problems with a Fedora Core 14 Linux machine. I inherited it recently from my late brother and while he was a Linux GOD, I am merely a mortal. I know something, somewhat about Linux from my days as a contributing editor at Newsforge (talk about embarrassing, asking this when I used to WRITE about Linux), but I do not know enough to solve this problem.</p><p>Anyway, I have traffic captures that look exactly, I mean EXACTLY like the dns-remoteshell.pcap (from the wireshark wiki under viruses and worms), but I don't know what to do NOW. Added bonus, my ISP is Hughesnet and I am getting slammed for going over their arbitrary and VERY low traffic caps. It's drive me WILD. I've been working on this for four days now and finding the pcap was a big breakthrough, but I don't know how to get rid of the worm(?), fix the problem or make this computer work right again. I am beginning to think that my best bet might be to wipe Fedora 14 and use freaking Windows which at least I understand. How is THAT for frustrated, PLEASE will someone trade me for a Mac!</p><p>Can someone help me, please!</p><p>UPDATE: whoops! neglected to mention that I've run a full scan with ClamAV with up to date signatures. And this seems to infect more than one user account.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-virus" rel="tag" title="see questions tagged &#39;virus&#39;">virus</span> <span class="post-tag tag-link-remoteshell" rel="tag" title="see questions tagged &#39;remoteshell&#39;">remoteshell</span> <span class="post-tag tag-link-worm" rel="tag" title="see questions tagged &#39;worm&#39;">worm</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '11, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/9aec1af73ba953c7d8d2ced8b9b5e85a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="privateice&#39;s gravatar image" /><p><span>privateice</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="privateice has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Aug '11, 06:42</strong> </span></p></div></div><div id="comments-container-5620" class="comments-container"><span id="5630"></span><div id="comment-5630" class="comment"><div id="post-5630-score" class="comment-score"></div><div class="comment-text"><p>SYNbit, Clam AV says nothing is infected with anything. It says the whole filesystem is clean.</p><p>The traffic I get has the Source Intel_some-address broadcasting a Who has for my IP. Then it does a lot of TCP requests for something or other. As far as I can tell, it uses those to download a huge amount of material--as much as the bandwidth can stand (which completely overwhelms my hughesnet at home).</p></div><div id="comment-5630-info" class="comment-info"><span class="comment-age">(10 Aug '11, 11:25)</span> <span class="comment-user userinfo">privateice</span></div></div></div><div id="comment-tools-5620" class="comment-tools"></div><div class="clear"></div><div id="comment-5620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5626"></span>

<div id="answer-container-5626" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5626-score" class="post-score" title="current number of votes">0</div><span id="post-5626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The file dns-remoteshell.pcap shows packets to an infected Windows XP system where a remote shell seems to be enabled on the TCP DNS port (and also on the TELNET and HTTP ports for that matter). In which way does you captured traffic look "exactly" the same?</p><p>What does ClamAV tell you? Which files seem to be infected and what kind of infections does it report? That would be your starting point in searching for a cure.</p><p>This Q&amp;A site might be able to help you analyze your traffic, but for cleaning the box, you are better of at other more linux orientated sites. You might want to try <a href="http://superuser.com/">http://superuser.com/</a> or <a href="http://serverfault.com/">http://serverfault.com/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '11, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5626" class="comments-container"></div><div id="comment-tools-5626" class="comment-tools"></div><div class="clear"></div><div id="comment-5626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

