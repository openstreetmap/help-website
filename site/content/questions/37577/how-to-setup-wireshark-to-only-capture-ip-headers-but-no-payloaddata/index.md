+++
type = "question"
title = "how to setup wireshark to only capture IP headers , but no Payload/data"
description = '''Hi There ,  is it possible to configure wireshark to only capture IP headers , NO payload/data ? if there is a way , can we set it as a default setting and only administrator of the PC should be able to change this setting . is it possible ? please help advise .  Thank you very much .'''
date = "2014-11-04T20:49:00Z"
lastmod = "2014-11-05T03:56:00Z"
weight = 37577
keywords = [ "capture", "only", "headers" ]
aliases = [ "/questions/37577" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to setup wireshark to only capture IP headers , but no Payload/data](/questions/37577/how-to-setup-wireshark-to-only-capture-ip-headers-but-no-payloaddata)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37577-score" class="post-score" title="current number of votes">0</div><span id="post-37577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There ,</p><p>is it possible to configure wireshark to only capture IP headers , NO payload/data ? if there is a way , can we set it as a default setting and only administrator of the PC should be able to change this setting . is it possible ? please help advise .</p><p>Thank you very much .</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-only" rel="tag" title="see questions tagged &#39;only&#39;">only</span> <span class="post-tag tag-link-headers" rel="tag" title="see questions tagged &#39;headers&#39;">headers</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '14, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/c5d35510dedf1205e7bdd61c513ee539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pvsrnaidu&#39;s gravatar image" /><p><span>pvsrnaidu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pvsrnaidu has no accepted answers">0%</span></p></div></div><div id="comments-container-37577" class="comments-container"></div><div id="comment-tools-37577" class="comment-tools"></div><div class="clear"></div><div id="comment-37577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37584"></span>

<div id="answer-container-37584" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37584-score" class="post-score" title="current number of votes">0</div><span id="post-37584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When configuring a capture on an interface you can <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChCapEditInterfaceSettingsSection.html">limit the amount of bytes capture per packet</a>. Setting this parameter just right allows you to get the IP headers you seek. Mind you, if there are additional fields in front or in the IP header (like options), you have to accommodate for that amount as well. This causes inclusion of next protocol headers if these fields are not present. In short, the capture engine has no knowledge of where the IP header ends, hence cannot cutoff capture at that point. (This would be an interesting item to engineer into the packet filter)</p><p>These settings cannot be fixed in any way you described. From the looks of it it seems as though you should look into other means to capture / sanitize your traffic, before feeding it to Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '14, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-37584" class="comments-container"></div><div id="comment-tools-37584" class="comment-tools"></div><div class="clear"></div><div id="comment-37584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

