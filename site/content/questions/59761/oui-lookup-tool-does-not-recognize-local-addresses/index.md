+++
type = "question"
title = "OUI Lookup Tool - Does not recognize local addresses"
description = '''Wireshark and Wireshark OUI Looktup tool do not seem to recognize locally administrated OUIs.  According to https://en.wikipedia.org/wiki/MAC_address the first 3 octets/first-half of a MAC-48/EUI-48 Address, correspond to the OUI (e.g.: MAC = 06:00:00:xx:xx:xx, OUI = 06:00:00), and the 2nd least sig...'''
date = "2017-03-01T06:13:00Z"
lastmod = "2017-03-02T10:52:00Z"
weight = 59761
keywords = [ "oui", "wireshark" ]
aliases = [ "/questions/59761" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OUI Lookup Tool - Does not recognize local addresses](/questions/59761/oui-lookup-tool-does-not-recognize-local-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59761-score" class="post-score" title="current number of votes">0</div><span id="post-59761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark and Wireshark OUI Looktup tool do not seem to recognize locally administrated OUIs.</p><p>According to <a href="https://en.wikipedia.org/wiki/MAC_address">https://en.wikipedia.org/wiki/MAC_address</a> the first 3 octets/first-half of a MAC-48/EUI-48 Address, correspond to the OUI (e.g.: MAC = 06:00:00:xx:xx:xx, OUI = 06:00:00), and the 2nd least significant bit of its first octet is used to differentiate "Universally" and "Locally" administered addresses). In other words, if we convert 06 (Hex) to 00000110 (Binary), we can see that the U/L bit is set to one, which means that it a locally administered address.</p><p>Given this if we disable that bit, we get the matching "Universally Administered Address" 00000100 (Binary), 04 (Hex) -&gt; "04:00:00", hence my question:</p><p>Shouldn't "04:00:00" and "06:00:00" resolve on the OUI Lookup tool to the same organization?</p><ul><li>A4:B1:e9 -&gt; Technicolor</li><li>A6:B1:e9 -&gt; No Matches</li><li>90:35:6E -&gt; Vodafone Omnitel N.V.</li><li>92:35:6E -&gt; No Matches</li><li>04:02:1F -&gt; HUAWEI TECHNOLOGIES CO.,LTD</li><li>06:02:1F -&gt; No Matches</li></ul><p><em>"Universal vs. local[edit] Addresses can either be universally administered addresses or locally administered addresses. A universally administered address is uniquely assigned to a device by its manufacturer. The first three octets (in transmission order) identify the organization that issued the identifier and are known as the Organizationally Unique Identifier (OUI).[4] The remainder of the address (three octets for MAC-48 and EUI-48 or five for EUI-64) are assigned by that organization in nearly any manner they please, subject to the constraint of uniqueness. A locally administered address is assigned to a device by a network administrator, overriding the burned-in address. Universally administered and locally administered addresses are distinguished by setting the second-least-significant bit of the first octet of the address. This bit is also referred to as the U/L bit, short for Universal/Local, which identifies how the address is administered. If the bit is 0, the address is universally administered. If it is 1, the address is locally administered. In the example address 06-00-00-00-00-00 the first octet is 06 (hex), the binary form of which is 00000110, where the second-least-significant bit is 1. Therefore, it is a locally administered address.[7] Consequently, this bit is 0 in all OUIs."</em></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-oui" rel="tag" title="see questions tagged &#39;oui&#39;">oui</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '17, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/9cc8175485b23ef3e0327fcbf72e5508?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jrmfreitas&#39;s gravatar image" /><p><span>jrmfreitas</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jrmfreitas has no accepted answers">0%</span></p></div></div><div id="comments-container-59761" class="comments-container"></div><div id="comment-tools-59761" class="comment-tools"></div><div class="clear"></div><div id="comment-59761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59766"></span>

<div id="answer-container-59766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59766-score" class="post-score" title="current number of votes">3</div><span id="post-59766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>Consequently, this bit is 0 in all OUIs.</em></p><p>I think that's the point. If it's 1, then the first 3 octets no longer represent an OUI. Locally administered addresses can be set to anything by anyone, so you can't infer anything about what the OUI would be if the bit had been set to 0.</p><p>I'm sure there's another more authoritative source, but from <a href="http://www.thefullwiki.org/Locally_Administered_Address#Address_details">http://www.thefullwiki.org/Locally_Administered_Address#Address_details</a>:</p><p><em>"A locally administered address is assigned to a device by a network administrator, overriding the burned-in address. Locally administered addresses do not contain OUIs."</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '17, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59766" class="comments-container"><span id="59769"></span><div id="comment-59769" class="comment"><div id="post-59769-score" class="comment-score">2</div><div class="comment-text"><p>Here is a document from the IEEE Registration Authority:</p><p><a href="http://standards.ieee.org/develop/regauth/tut/eui.pdf">http://standards.ieee.org/develop/regauth/tut/eui.pdf</a></p><p>Page 4, paragraph 1 states: A CID has the X bit equal to one and consequently that places any address with the CID as its first three octets in the local address space (U/L = 1). Local addresses are not globally unique, but a network administrator is responsible for assuring that any local addresses assigned are unique within the span of use. (Uniqueness of local addresses typically does not need to extend beyond a router.)</p></div><div id="comment-59769-info" class="comment-info"><span class="comment-age">(01 Mar '17, 10:02)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="59771"></span><div id="comment-59771" class="comment"><div id="post-59771-score" class="comment-score"></div><div class="comment-text"><p>Thanks for providing the authoritative source! :)</p></div><div id="comment-59771-info" class="comment-info"><span class="comment-age">(01 Mar '17, 10:11)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="59808"></span><div id="comment-59808" class="comment"><div id="post-59808-score" class="comment-score"></div><div class="comment-text"><p>Thanks for sharing this documentation, your feedback does make sense :)</p></div><div id="comment-59808-info" class="comment-info"><span class="comment-age">(02 Mar '17, 10:52)</span> <span class="comment-user userinfo">jrmfreitas</span></div></div></div><div id="comment-tools-59766" class="comment-tools"></div><div class="clear"></div><div id="comment-59766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

