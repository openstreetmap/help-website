+++
type = "question"
title = "ZEP upgrade on Wireshark for linux Ubuntu"
description = '''Hi everyone,  First, I would like to thank all Wireshark contributors for making such a good product available to the community! I would like to to know if there is any plan to upgrade the ZigBee Encapsulation Protocol (ZEP) plugin from ZEPv2 to ZEPv4 for linux Ubuntu for Wireshark versions 2.2.X si...'''
date = "2017-09-28T15:59:00Z"
lastmod = "2017-09-29T02:18:00Z"
weight = 63668
keywords = [ "zep", "ubuntu", "sewio", "linux" ]
aliases = [ "/questions/63668" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ZEP upgrade on Wireshark for linux Ubuntu](/questions/63668/zep-upgrade-on-wireshark-for-linux-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63668-score" class="post-score" title="current number of votes">0</div><span id="post-63668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>First, I would like to thank all Wireshark contributors for making such a good product available to the community!</p><p>I would like to to know if there is any plan to upgrade the ZigBee Encapsulation Protocol (ZEP) plugin from ZEPv2 to ZEPv4 for linux Ubuntu for Wireshark versions 2.2.X since sniffers vendors such as SEWIO seem to have ended their support to this very important/simple feature within Wireshark</p><p>Please check the features added by their ZEP v3 and V4 at <a href="https://www.sewio.net/open-sniffer/sniffer-installation/">https://www.sewio.net/open-sniffer/sniffer-installation/</a> ---&gt;select the "Part 3 - Adjusting Wireshark" tab</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zep" rel="tag" title="see questions tagged &#39;zep&#39;">zep</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-sewio" rel="tag" title="see questions tagged &#39;sewio&#39;">sewio</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '17, 15:59</strong></p><img src="https://secure.gravatar.com/avatar/74e0743a7d5d9cbc34c799d4a7255f82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireless_adapter_rf&#39;s gravatar image" /><p><span>wireless_ada...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireless_adapter_rf has no accepted answers">0%</span></p></div></div><div id="comments-container-63668" class="comments-container"></div><div id="comment-tools-63668" class="comment-tools"></div><div class="clear"></div><div id="comment-63668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63670"></span>

<div id="answer-container-63670" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63670-score" class="post-score" title="current number of votes">0</div><span id="post-63670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are a couple of things to say in response:</p><ol><li>There is no formal planning of supported features, see <a href="https://www.wireshark.org/faq.html#q1.11">the FAQ</a></li><li>New features are only introduced into the development version, later to become the stable version, see <a href="https://wiki.wireshark.org/Development/LifeCycle">the life cycle.</a></li><li>Since the <a href="https://www.gnu.org/licenses/gpl-2.0.html">GPLv2</a> applies to Wireshark and therefore to this dissector by SEWIO, you can request its source code from them and work with the Wireshark developers to get it into the repository.</li></ol><p>I have no working knowledge of this protocol so can't comment on its relevance.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '17, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63670" class="comments-container"></div><div id="comment-tools-63670" class="comment-tools"></div><div class="clear"></div><div id="comment-63670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

