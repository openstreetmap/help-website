+++
type = "question"
title = "How to add Cisco vendor specific AVPs in wireshark for OS X?"
description = '''Hi  I have tried following options but the Cisco vendor specific AVPs are not decoded in wireshark for Mac. -&amp;gt;Add the new AVPs in Cisco.xml(vendor-id=&quot;Cisco&quot;) which is located at /Applications/Wireshark.app/Contents/Resources/share/wireshark/diameter directory and relaunch the wireshark. -&amp;gt;Add...'''
date = "2014-11-13T14:29:00Z"
lastmod = "2014-11-14T07:40:00Z"
weight = 37843
keywords = [ "cisco" ]
aliases = [ "/questions/37843" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add Cisco vendor specific AVPs in wireshark for OS X?](/questions/37843/how-to-add-cisco-vendor-specific-avps-in-wireshark-for-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37843-score" class="post-score" title="current number of votes">0</div><span id="post-37843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have tried following options but the Cisco vendor specific AVPs are not decoded in wireshark for Mac.</p><p>-&gt;Add the new AVPs in Cisco.xml(vendor-id="Cisco") which is located at /Applications/Wireshark.app/Contents/Resources/share/wireshark/diameter directory and relaunch the wireshark.</p><p>-&gt;Add the new AVPs in dictionary.xml(vendor-id="Cisco") which is located at /Applications/Wireshark.app/Contents/Resources/share/wireshark/diameter directory and relaunch the wireshark.</p><p>-&gt;Add the new AVPs in dictionary.xml(vendor-id="TGPP") which is located at /Applications/Wireshark.app/Contents/Resources/share/wireshark/diameter directory and relaunch the wireshark.</p><p>Can someone please help out in resolving this problem?</p><p>Regards Sushil</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '14, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/f169be41b5c09d4ede836d9ea495c648?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SSushilK&#39;s gravatar image" /><p><span>SSushilK</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SSushilK has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '14, 20:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-37843" class="comments-container"></div><div id="comment-tools-37843" class="comment-tools"></div><div class="clear"></div><div id="comment-37843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37847"></span>

<div id="answer-container-37847" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37847-score" class="post-score" title="current number of votes">0</div><span id="post-37847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Either of the first two should work.</p><p>That assumes, of course, that</p><ol><li>the AVPs in your message actually have the V bit set</li><li>(and) the Vendor-ID in the AVP is 5771</li></ol><p>I would also encourage you to submit your changes and a sample capture to the <a href="https://bugs.wireshark.org">bug database</a> so those AVPs could be added to future versions of Wireshark. (If it still doesn't work for you then someone could also help figure out what's going wrong.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '14, 17:44</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37847" class="comments-container"><span id="37848"></span><div id="comment-37848" class="comment"><div id="post-37848-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff for the quick response. Actually, the message has the Cisco specific AVPs with V bit set and Vendor-Id set to 9. If the Vendor-Id is expected to be 5771, how do we add the rule in the xml file to process the AVPs with Vendor-Id set to 9 since the format in xml is like vendor-id="Cisco"? Thanks in Advance!</p></div><div id="comment-37848-info" class="comment-info"><span class="comment-age">(13 Nov '14, 20:44)</span> <span class="comment-user userinfo">SSushilK</span></div></div><span id="37849"></span><div id="comment-37849" class="comment"><div id="post-37849-score" class="comment-score">1</div><div class="comment-text"><p>In dictionary.xml, add vendor id for cisco-systems with the value of 9 and name cisco-systems then add the AVP to cisco.xml with the vendoriset to cisco-systems.</p></div><div id="comment-37849-info" class="comment-info"><span class="comment-age">(13 Nov '14, 21:16)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="37862"></span><div id="comment-37862" class="comment"><div id="post-37862-score" class="comment-score"></div><div class="comment-text"><p>Thanks Anders. It worked after making the suggested changes.</p></div><div id="comment-37862-info" class="comment-info"><span class="comment-age">(14 Nov '14, 07:40)</span> <span class="comment-user userinfo">SSushilK</span></div></div></div><div id="comment-tools-37847" class="comment-tools"></div><div class="clear"></div><div id="comment-37847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

