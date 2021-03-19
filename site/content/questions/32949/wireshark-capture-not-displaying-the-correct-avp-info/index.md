+++
type = "question"
title = "Wireshark capture not displaying the correct AVP info"
description = '''I have just downloaded the latest version of Wireshark 1.10.7. I&#x27;ve just done a capture looking at Radius messages and I noticed it&#x27;s not displaying the correct vendor info in Access-Accept. In the Access-Accept message, under Radius Protocol, Attribute Value Pairs: - Radius Protocol  - Attribute Va...'''
date = "2014-05-21T05:32:00Z"
lastmod = "2014-05-21T18:44:00Z"
weight = 32949
keywords = [ "radius" ]
aliases = [ "/questions/32949" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark capture not displaying the correct AVP info](/questions/32949/wireshark-capture-not-displaying-the-correct-avp-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32949-score" class="post-score" title="current number of votes">0</div><span id="post-32949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have just downloaded the latest version of Wireshark 1.10.7. I've just done a capture looking at Radius messages and I noticed it's not displaying the correct vendor info in Access-Accept.</p><p>In the Access-Accept message, under Radius Protocol, Attribute Value Pairs: - Radius Protocol - Attribute Value Pairs + AVP: l=24 t=Vendor-Specific(26) v=Panthera Networks, Inc.(6527)</p><p>In an earlier version of Wireshark 1.6.5 (admittedly on a different computer), this is decoded correctly as - Radius Protocol - Attribute Value Pairs + AVP: l=24 t=Vendor-Specific(26) v=Alcatel-Lucent-Service-Router(6527)</p><p>Is there something I've missed in the installation where the 1.10.7 version cannot recognise 6527?<br />
</p><p>Perhaps, I'm barking up the wrong tree, Within the Wireshark -&gt; radius folder, I do have a file called 'dictionary.alcatel.sr' and in the dictionary.xml file, there is a line: $INCLUDE dictionary.alcatel.sr</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '14, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/993757ab6c5b491a5b5dc795c4664290?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KenLam&#39;s gravatar image" /><p><span>KenLam</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KenLam has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-32949" class="comments-container"><span id="32960"></span><div id="comment-32960" class="comment"><div id="post-32960-score" class="comment-score"></div><div class="comment-text"><blockquote><p>in the dictionary.xml file, there is a line: $INCLUDE dictionary.alcatel.sr You actually mean the file Dictionary in ~/radius not ~/diameter/dictionary.xml - right?</p></blockquote></div><div id="comment-32960-info" class="comment-info"><span class="comment-age">(21 May '14, 13:45)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-32949" class="comment-tools"></div><div class="clear"></div><div id="comment-32949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32959"></span>

<div id="answer-container-32959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32959-score" class="post-score" title="current number of votes">1</div><span id="post-32959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In sminmpec.c which is generated from <a href="http://www.iana.org/assignments/enterprise-numbers">http://www.iana.org/assignments/enterprise-numbers</a> 6527 <em>is</em> listed as: { 6527, "Panthera Networks, Inc." },</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '14, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32959" class="comments-container"></div><div id="comment-tools-32959" class="comment-tools"></div><div class="clear"></div><div id="comment-32959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32970"></span>

<div id="answer-container-32970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32970-score" class="post-score" title="current number of votes">1</div><span id="post-32970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's some history to this one. The short answer is that Anders is write (Wireshark's code is written based on the IANA registry, and IANA registers the number as Panthera Networks, Inc). However, this explains it a bit ( <a href="http://www.circitor.fr/Mibs/Files/TIMETRA-GLOBAL-MIB.mib">http://www.circitor.fr/Mibs/Files/TIMETRA-GLOBAL-MIB.mib</a> ):</p><p>"The Private Enterprise Number 6527 was assigned to TiMetra Inc., previously known as Panthera Networks, by the IANA on July 14, 2000. TiMetra, Inc. was acquired by Alcatel on July 18, 2003 and has had the timetra enterprise number, 6527, registered to Alcatel."</p><p>Further, I can say that some Alcatel routers use that number for SNMP MIBs and decode it simply as "Alcatel" in logs. It's odd since that source claims 6527 was changed to "Alcatel" and Wireshark's older version's source code would suggest it used to, indeed, be Alcatel, so it looks like the IANA may have changed it back (?).</p><p>Either way, It's not Wireshark's problem. If the name is wrong and you are the owner, you would need to submit a request to the IANA with this web form: <a href="http://pen.iana.org/pen/ModifyPen.page">http://pen.iana.org/pen/ModifyPen.page</a></p><p>And if you're not the owner, then you have no standing to have this changed, nor would it make sense for Wireshark to not list these numbers as the IANA reference indicates.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '14, 18:44</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 May '14, 21:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-32970" class="comments-container"></div><div id="comment-tools-32970" class="comment-tools"></div><div class="clear"></div><div id="comment-32970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

