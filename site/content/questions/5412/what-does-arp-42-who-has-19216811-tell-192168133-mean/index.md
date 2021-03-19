+++
type = "question"
title = "What does arp 42 who has 192.168.1.1? tell 192.168.1.33 mean?"
description = '''What does this mean?  arp 42 who has 192.168.1.1? tell 192.168.1.33&quot; '''
date = "2011-08-02T17:18:00Z"
lastmod = "2016-06-05T09:33:00Z"
weight = 5412
keywords = [ "arp" ]
aliases = [ "/questions/5412" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What does arp 42 who has 192.168.1.1? tell 192.168.1.33 mean?](/questions/5412/what-does-arp-42-who-has-19216811-tell-192168133-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5412-score" class="post-score" title="current number of votes">1</div><span id="post-5412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What does this mean?</p><p>arp 42 who has 192.168.1.1? tell 192.168.1.33"</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '11, 17:18</strong></p><img src="https://secure.gravatar.com/avatar/fef555bbaf34cae978950cd07488b009?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandra%20Wolfe&#39;s gravatar image" /><p><span>Sandra Wolfe</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandra Wolfe has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Aug '11, 17:19</strong> </span></p></div></div><div id="comments-container-5412" class="comments-container"><span id="53209"></span><div id="comment-53209" class="comment"><div id="post-53209-score" class="comment-score"></div><div class="comment-text"><p>It seems my Samsung TV keeps sending these same ARP requests nonstop. what is weird is my samsung tv gets internet access just fine and when i check the Default Gateway on my TV it matches the default gateway of my router just fine. So are these non-stop requests normal?</p><p>arp 42 who has 192.168.1.1? tell 192.168.1.33"</p></div><div id="comment-53209-info" class="comment-info"><span class="comment-age">(05 Jun '16, 07:45)</span> <span class="comment-user userinfo">Neoraj3</span></div></div><span id="53210"></span><div id="comment-53210" class="comment"><div id="post-53210-score" class="comment-score"></div><div class="comment-text"><p>It should have probably been a separate Question. Nevertheless:</p><p>Various types of equipment use ARP requests to continuously monitor availability of LAN connection in general and the router in particular, i.e. they keep sending ARP requests even when it doesn't acutely need to send any data.</p></div><div id="comment-53210-info" class="comment-info"><span class="comment-age">(05 Jun '16, 09:33)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-5412" class="comment-tools"></div><div class="clear"></div><div id="comment-5412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5414"></span>

<div id="answer-container-5414" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5414-score" class="post-score" title="current number of votes">6</div><span id="post-5414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sandra Wolfe has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The host with IP address 192.168.1.33 wants to send some data. It knows it must send this data to 192.168.1.1, but it doesn't know the MAC address to send it to, so it has sent an Address Resolution Protocol (ARP) request to find out that information.</p><p>So, arp stands for "Address Resolution Protocol", and 42 is the number of bytes comprising this ARP packet. And since 42 is less than the minimum number of bytes for an Ethernet frame, it also means that you were capturing on the same machine that sent the ARP request, in this case, 192.168.1.33.</p><p>For more information about ARP, refer to sites such as:</p><ul><li><a href="http://en.wikipedia.org/wiki/Address_Resolution_Protocol">http://en.wikipedia.org/wiki/Address_Resolution_Protocol</a></li><li><a href="http://www.networksorcery.com/enp/protocol/arp.htm">http://www.networksorcery.com/enp/protocol/arp.htm</a></li><li><a href="http://wiki.wireshark.org/AddressResolutionProtocol">http://wiki.wireshark.org/AddressResolutionProtocol</a></li><li><a href="http://tools.ietf.org/html/rfc826">RFC 826</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '11, 19:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-5414" class="comments-container"></div><div id="comment-tools-5414" class="comment-tools"></div><div class="clear"></div><div id="comment-5414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

