+++
type = "question"
title = "US Number Portability decode"
description = '''Trying to trace US Number portability using wireshark but I am getting the following decode below :( ANSI Transaction Capabilities Application Part  response  identifier: 2b40012a  componentPortion: 1 item  ComponentPDU: invokeLast (9)  invokeLast  componentIDs: 0000  operationCode: national (16)  n...'''
date = "2016-07-18T11:14:00Z"
lastmod = "2016-07-18T13:11:00Z"
weight = 54136
keywords = [ "tcap", "ansi", "not", "decode", "implimented" ]
aliases = [ "/questions/54136" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [US Number Portability decode](/questions/54136/us-number-portability-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54136-score" class="post-score" title="current number of votes">0</div><span id="post-54136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to trace US Number portability using wireshark but I am getting the following decode below :(</p><pre><code>ANSI Transaction Capabilities Application Part
    response
        identifier: 2b40012a
        componentPortion: 1 item
            ComponentPDU: invokeLast (9)
                invokeLast
                    componentIDs: 0000
                    operationCode: national (16)
                        national: 1025
                            0... .... .... .... = Require Reply: False
                            .000 0100 .... .... = Family: Connection Control (4)
                            .... .... 0000 0001 = Specifier: 1 Connect
                    Dissector for ANSI TCAP NATIONAL code:0x401(Family 4, Specifier 1) 
not implemented. Contact Wireshark developers if you want this supported(Spec required)
                        [Expert Info (Warn/Undecoded): Dissector for ANSI TCAP NATIONAL code:0x401(Family 4, Specifier 1) 
not implemented. Contact Wireshark developers if you want this supported(Spec required)]
                            [Dissector for ANSI TCAP NATIONAL code:0x401(Family 4, Specifier 1) 
not implemented. Contact Wireshark developers if you want this supported(Spec required)]
                            [Severity level: Warn]
                            [Group: Undecoded]
                    BER Error: This field lies beyond the end of the known sequence definition.
                        [Expert Info (Warn/Malformed): BER Error: Unknown field in Sequence]
                            [BER Error: Unknown field in Sequence]
                            [Severity level: Warn]
                            [Group: Malformed]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcap" rel="tag" title="see questions tagged &#39;tcap&#39;">tcap</span> <span class="post-tag tag-link-ansi" rel="tag" title="see questions tagged &#39;ansi&#39;">ansi</span> <span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-implimented" rel="tag" title="see questions tagged &#39;implimented&#39;">implimented</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '16, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/4bc0fe37a8150f1e564b5943078ed660?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Pierotti&#39;s gravatar image" /><p><span>Michael Pier...</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Pierotti has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jul '16, 13:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-54136" class="comments-container"></div><div id="comment-tools-54136" class="comment-tools"></div><div class="clear"></div><div id="comment-54136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54139"></span>

<div id="answer-container-54139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54139-score" class="post-score" title="current number of votes">1</div><span id="post-54139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the printout says, a publicly available protocol specification is needed to write a dissector for the protocol. No dissector is currently available.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '16, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-54139" class="comments-container"><span id="54143"></span><div id="comment-54143" class="comment"><div id="post-54143-score" class="comment-score"></div><div class="comment-text"><p>Just to add to that: if you have a specification and a sample capture that you can share then open an <a href="https://bugs.wireshark.org">enhancement request</a> (and attach both to the request) asking for dissection support.</p></div><div id="comment-54143-info" class="comment-info"><span class="comment-age">(18 Jul '16, 13:11)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-54139" class="comment-tools"></div><div class="clear"></div><div id="comment-54139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

