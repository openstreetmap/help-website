+++
type = "question"
title = "Can only see multicast and local traffic"
description = '''I have installed Wireshark on a Macmini with osx 10.6. When I capture, the trafic only consists of broadcasts and local trafic. I cant see http-trafic of other computers in the wireless-net. I have choosen the airport interface and I have choosen ethernet ( If I choose any of the 802 I get nothing )...'''
date = "2011-02-28T22:51:00Z"
lastmod = "2011-03-02T10:44:00Z"
weight = 2591
keywords = [ "osx", "macintosh" ]
aliases = [ "/questions/2591" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can only see multicast and local traffic](/questions/2591/can-only-see-multicast-and-local-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2591-score" class="post-score" title="current number of votes">0</div><span id="post-2591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed Wireshark on a Macmini with osx 10.6. When I capture, the trafic only consists of broadcasts and local trafic. I cant see http-trafic of other computers in the wireless-net. I have choosen the airport interface and I have choosen ethernet ( If I choose any of the 802 I get nothing ).</p><p>Do I have to buy another interface? ( A usb domngle? ) cause Apples own doesnt allow this traffic or what?</p><p>/ Mid</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-macintosh" rel="tag" title="see questions tagged &#39;macintosh&#39;">macintosh</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '11, 22:51</strong></p><img src="https://secure.gravatar.com/avatar/53c8cb9e7ca6f4dffbebd9ecf7b83f32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="midmus&#39;s gravatar image" /><p><span>midmus</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="midmus has no accepted answers">0%</span></p></div></div><div id="comments-container-2591" class="comments-container"></div><div id="comment-tools-2591" class="comment-tools"></div><div class="clear"></div><div id="comment-2591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2603"></span>

<div id="answer-container-2603" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2603-score" class="post-score" title="current number of votes">0</div><span id="post-2603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Even in promiscuous mode, if you're not in monitor mode, the adapter will probably receive only unicast traffic to your machine and broadcast/multicast traffic. In monitor mode, it <em>should</em> see other traffic. If you're offered a choice of Ethernet headers or 802.11 headers, you're presumably running a version of Wireshark that doesn't handle the new "turn on monitor mode" APIs, in which case the way you turn on monitor mode is to select 802.11 headers - in monitor mode, I've been able to capture traffic that's neither to my machine nor from my machine nor broadcast/multicast.</p><p>Now, be aware that if you're on a WEP or WPA network, you will not be able to see that traffic as anything other than 802.11 packets without the network password - you won't even be able to see the IP headers! - and, on a WPA network, you won't be able to see it as anything other than 802.11 even <em>with</em> the password unless you've captured the setup packets. Are you not seeing <em>any</em> packets in monitor mode, or are you seeing lots of packets that are reported as just 802.11 data packets?</p><p>(This is not Mac-specific, by the way.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '11, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2603" class="comments-container"><span id="2627"></span><div id="comment-2627" class="comment"><div id="post-2627-score" class="comment-score"></div><div class="comment-text"><p>Thanx for the answer, I get you. It's WShark version 1.4.3 for Mac OSX I'm using. So I am right that it is the adapter that gives me the restriction? As it should see all traffic on a wireless net right? I mean a wireless net isnt switched :) / Mid</p></div><div id="comment-2627-info" class="comment-info"><span class="comment-age">(02 Mar '11, 02:14)</span> <span class="comment-user userinfo">midmus</span></div></div><span id="2636"></span><div id="comment-2636" class="comment"><div id="post-2636-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "see" in "see all traffic" and "get nothing" in "If I choose any of the 802 I get nothing"? Do you mean <em>NO</em> packets show up in Wireshark's packet list when you capture, or do you mean you don't see HTTP traffic? If it's the latter, the adapter is doing the right thing, you're probably on a WEP or WPA network and haven't supplied the password for the network.</p></div><div id="comment-2636-info" class="comment-info"><span class="comment-age">(02 Mar '11, 10:44)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-2603" class="comment-tools"></div><div class="clear"></div><div id="comment-2603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

