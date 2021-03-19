+++
type = "question"
title = "managing Filters inside Profile Preferences files"
description = '''I want to more effectively manage Filters defined within Profiles. By that, I mean that each of my Profiles tends to contain the same basic set of Filters, plus a bunch which are unique to that Profile, and that I occasionally want to update that common set. Specifically, %APPDATA%&#92;Wireshark&#92;profile...'''
date = "2015-01-08T06:42:00Z"
lastmod = "2015-01-10T05:51:00Z"
weight = 38956
keywords = [ "profile", "filter", "preference" ]
aliases = [ "/questions/38956" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [managing Filters inside Profile Preferences files](/questions/38956/managing-filters-inside-profile-preferences-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38956-score" class="post-score" title="current number of votes">0</div><span id="post-38956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to more effectively manage Filters defined within Profiles.</p><p>By that, I mean that each of my Profiles tends to contain the same basic set of Filters, plus a bunch which are unique to that Profile, and that I occasionally want to update that common set.</p><p>Specifically, %APPDATA%\Wireshark\profiles{name of profile}\preferences contains a section which looks like this:</p><h6 id="filter-expressions"># Filter Expressions</h6><p>gui.filter_expressions.label: Me gui.filter_expressions.enabled: TRUE gui.filter_expressions.expr: eth.addr==80:EE:73:43:D6:9C gui.filter_expressions.label: Not Broadcast gui.filter_expressions.enabled: TRUE gui.filter_expressions.expr: not eth.ig==1 gui.filter_expressions.label: Not-Junk gui.filter_expressions.enabled: TRUE gui.filter_expressions.expr: not (browser or db-lsp-disc or ipv6 or ip.dst==224.0.0.0/8 or hsrp or ipx or nbns or rtmp or stp) gui.filter_expressions.label: TAF gui.filter_expressions.enabled: TRUE gui.filter_expressions.expr: (tcp.analysis.flags and not tcp.analysis.window_update) or tcp.flags.reset==1 gui.filter_expressions.label: TCP Reset gui.filter_expressions.enabled: TRUE gui.filter_expressions.expr: tcp.flags.reset==1</p><p>When I copy my Profile collection to a new machine (which happens more frequently than I'm enjoying), I manually edit each preferences file and change '80:EE:73:43:D6:9C' to the MAC address of my new workstation. Tedious.</p><p>In a perfect world, I would paste this block of 'common' filters into %APPDATA%\Roaming\Wireshark\preferences or perhaps preferences_common; then, they would magically appear in every single Profile ... and life would be good. But, we don't yet have a concept of a 'common' preferences file, per <a href="https://www.wireshark.org/lists/wireshark-users/201306/msg00041.html">https://www.wireshark.org/lists/wireshark-users/201306/msg00041.html</a> [The approach I'm imagining would also make it easy to add a new filter to every single Profile ... or to update the 'Not Junk' filter, the elements of which are gradually increasing as I encounter more and more 'junk' in my environments ... both currently manual / tedious tasks.]</p><p>So I'm headed toward writing a Windows .bat file and a *nix bash script to at least automate replacing '80:EE:73:43:D6:9C' with the MAC address of my new workstation. A little directory traversal, a sed one-liner, not too difficult.</p><p>But before I walk this path, I want to float this problem here, figuring that other folks face it too. Has anyone tumbled to a more clever solution than the one I'm envisioning?</p><p>--sk</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-profile" rel="tag" title="see questions tagged &#39;profile&#39;">profile</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-preference" rel="tag" title="see questions tagged &#39;preference&#39;">preference</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '15, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/18ae5b8bfddad49931ec557b9342075a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skendric&#39;s gravatar image" /><p><span>skendric</span><br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skendric has no accepted answers">0%</span></p></div></div><div id="comments-container-38956" class="comments-container"></div><div id="comment-tools-38956" class="comment-tools"></div><div class="clear"></div><div id="comment-38956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39023"></span>

<div id="answer-container-39023" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39023-score" class="post-score" title="current number of votes">0</div><span id="post-39023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Has anyone tumbled to a more clever solution than the one I'm envisioning?<br />
eth.addr==80:EE:73:43:D6:9C gui.filter_expressions.label: <strong>Not Broadcast</strong></p></blockquote><p>Instead of rewriting your MAC address, you could use the following, common filter, to remove <strong>ethernet broadcasts</strong></p><blockquote><p>!eth.addr==FF:FF:FF:FF:FF:FF</p></blockquote><p>This will however only filter <strong>broadcast</strong> MAC addresses, not <strong><a href="http://en.wikipedia.org/wiki/Multicast_address#Ethernet">multicast MAC addresses</a></strong>, but maybe that's O.K. for your environment.</p><p>Unfortunately the following filter does not work to remove the most common multicast MAC addresses.</p><blockquote><p>! eth.addr matches "^(01|33)"</p></blockquote><p>Whereas the following filter returns the correct frames!?!</p><blockquote><p>eth.addr matches "^33"</p></blockquote><p>However <strong>not</strong> this filter!</p><blockquote><p>eth.addr matches "^01"</p></blockquote><p>So, either the "matches" operator is either buggy when applied to eth.addr fields, or it works differently than I would have expected.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '15, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-39023" class="comments-container"></div><div id="comment-tools-39023" class="comment-tools"></div><div class="clear"></div><div id="comment-39023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

