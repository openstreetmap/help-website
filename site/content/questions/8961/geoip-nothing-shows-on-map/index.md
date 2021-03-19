+++
type = "question"
title = "GeoIP Nothing Shows on Map"
description = '''I have GeoIP configured in Wireshark, and when I go to Statistics &amp;gt; Endpoints and click on the IPv4 tab, I see location information, including latitude and longitude. However, when I click on the Map button, I always get a blank map; no locations are shown. I&#x27;m using IE 8. When I click the Map bu...'''
date = "2012-02-10T19:57:00Z"
lastmod = "2013-12-08T21:56:00Z"
weight = 8961
keywords = [ "geoip" ]
aliases = [ "/questions/8961" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [GeoIP Nothing Shows on Map](/questions/8961/geoip-nothing-shows-on-map)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8961-score" class="post-score" title="current number of votes">0</div><span id="post-8961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have GeoIP configured in Wireshark, and when I go to Statistics &gt; Endpoints and click on the IPv4 tab, I see location information, including latitude and longitude. However, when I click on the Map button, I always get a blank map; no locations are shown.</p><p>I'm using IE 8. When I click the Map button, I get a bar across the top that says "To help protect your security, Internet Explorer has restricted this page from running scripts or ActiveX controls that could access your computer. Click here for options." I click on the bar, and then click "Allow Blocked Content..." I get a second warning that ends with "Are you sure you want to let this file run active content?" I click "Yes," and the map appears, but there are never any location points shown.</p><p>Any ideas on why I'm getting location information, but not seeing the locations on the map?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-geoip" rel="tag" title="see questions tagged &#39;geoip&#39;">geoip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '12, 19:57</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '12, 21:34</strong> </span></p></div></div><div id="comments-container-8961" class="comments-container"><span id="8962"></span><div id="comment-8962" class="comment"><div id="post-8962-score" class="comment-score">1</div><div class="comment-text"><p>I never got it working with IE. I use Mozilla Firefox (set Firefox as default browser).</p></div><div id="comment-8962-info" class="comment-info"><span class="comment-age">(10 Feb '12, 22:34)</span> <span class="comment-user userinfo">joke</span></div></div><span id="8964"></span><div id="comment-8964" class="comment"><div id="post-8964-score" class="comment-score"></div><div class="comment-text"><p>That did it. I just made Firefox the default browser. I did not change any settings, and it worked immediately.</p></div><div id="comment-8964-info" class="comment-info"><span class="comment-age">(11 Feb '12, 13:49)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="13959"></span><div id="comment-13959" class="comment"><div id="post-13959-score" class="comment-score"></div><div class="comment-text"><p>I'm getting all the GeoIP lacation info as well, but I get a blank browser page in Firefox, Chrome, and IE. Java script is enabled. No pop-up issues or warnings either. I can open a browser within Wireshark, e.g. Help/Website just fine. Both Wireshark 1.6 and 1.8 have the same problem. I'm running on Win7 64bit, any ideas?</p></div><div id="comment-13959-info" class="comment-info"><span class="comment-age">(29 Aug '12, 13:16)</span> <span class="comment-user userinfo">GoogleShark</span></div></div></div><div id="comment-tools-8961" class="comment-tools"></div><div class="clear"></div><div id="comment-8961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8965"></span>

<div id="answer-container-8965" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8965-score" class="post-score" title="current number of votes">0</div><span id="post-8965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the GeoIP mapping stuff is, for example, generating Web pages that use Javascript, perhaps IE is being more paranoid here than Firefox, and perhaps either that, or (*sigh*) browser differences in the handling of Javascript, or both, are causing the problem.</p><p>You should probably file a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> for this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '12, 18:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '12, 21:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-8965" class="comments-container"><span id="8968"></span><div id="comment-8968" class="comment"><div id="post-8968-score" class="comment-score"></div><div class="comment-text"><blockquote><p>You should probably file a bug on the Wireshark Bugzilla for this.</p></blockquote><p>Done. Bug 6834.</p></div><div id="comment-8968-info" class="comment-info"><span class="comment-age">(11 Feb '12, 20:58)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-8965" class="comment-tools"></div><div class="clear"></div><div id="comment-8965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14649"></span>

<div id="answer-container-14649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14649-score" class="post-score" title="current number of votes">0</div><span id="post-14649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The bug that caused this problem, tracked in Wireshark's bugzilla database as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5016">bug 5016</a> (of which there were several duplicates including bugs <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6834">6834</a>, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7040">7040</a>, and <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7540">7540</a>) has been fixed in the just-released Wireshark 1.8.3 and 1.6.11 versions. Visit the Wireshark <a href="http://www.wireshark.org/download.html">download</a> page to download and update your version of Wireshark in order to fix this problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '12, 19:04</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-14649" class="comments-container"><span id="27910"></span><div id="comment-27910" class="comment"><div id="post-27910-score" class="comment-score"></div><div class="comment-text"><p>I'm running Latest version of Wireshark with Windows 8.1 64 Bit</p><p>When the map loads all the Tiles show as broken images. although the location data is itself plotted. Tested with Chrome, Firefox and IE11</p></div><div id="comment-27910-info" class="comment-info"><span class="comment-age">(07 Dec '13, 23:46)</span> <span class="comment-user userinfo">ravenstar68</span></div></div><span id="27941"></span><div id="comment-27941" class="comment"><div id="post-27941-score" class="comment-score"></div><div class="comment-text"><p>Not sure what's changed but the map has now started working for me in all my browsers.</p><p>If it's down to you guys then thanks.</p><p>Ravenstar68</p></div><div id="comment-27941-info" class="comment-info"><span class="comment-age">(08 Dec '13, 21:56)</span> <span class="comment-user userinfo">ravenstar68</span></div></div></div><div id="comment-tools-14649" class="comment-tools"></div><div class="clear"></div><div id="comment-14649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

