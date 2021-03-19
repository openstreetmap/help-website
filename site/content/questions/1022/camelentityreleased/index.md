+++
type = "question"
title = "camel.EntityReleased"
description = '''What is the correct format for the entity released camel function? The 3GPP document says it should be: Entity released  -&amp;gt;Call Segment Failure  -&amp;gt;CallSegmentID  -&amp;gt;Cause  -&amp;gt;BCSM Failure  -&amp;gt;LegID  -&amp;gt;Cause  But this causes a &#x27;BER Error - This field lies beyond the end of the known se...'''
date = "2010-11-19T08:24:00Z"
lastmod = "2010-11-19T08:24:00Z"
weight = 1022
keywords = [ "ber", "camel", "entityreleased", "error", "format" ]
aliases = [ "/questions/1022" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [camel.EntityReleased](/questions/1022/camelentityreleased)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1022-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the correct format for the entity released camel function? The 3GPP document says it should be: Entity released</p><pre><code>      -&gt;Call Segment Failure
                 -&gt;CallSegmentID
                 -&gt;Cause
      -&gt;BCSM Failure
                 -&gt;LegID
                 -&gt;Cause</code></pre><p>But this causes a 'BER Error - This field lies beyond the end of the known sequence definition' message. I've seen references elsewhere saying that entityReleased is boolean. Any help would be appreciated!</p></div><div id="question-tags" class="tags-container tags">ber camel entityreleased error format</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '10, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/500a1903ac7d35a475f37da84357748f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbartlett2010&#39;s gravatar image" /><p>dbartlett2010<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbartlett2010 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Nov '10, 08:24</p></div></div><div id="comments-container-1022" class="comments-container"><span id="1024"></span><div id="comment-1024" class="comment"><div id="post-1024-score" class="comment-score"></div><div class="comment-text"><p>3GPP TS 29.078 9.2.0 (2010-06) has it as</p><p>EntityReleasedArg {PARAMETERS-BOUND : bound} ::= CHOICE {</p><pre><code>callSegmentFailure                  [0] CallSegmentFailure {bound},
bCSM-Failure                    [1] BCSM-Failure {bound}
}</code></pre><p>I don't know if it was defined differently in earlier specs. You could open up a bug report at https://bugs.wireshark.org/bugzilla/ enclosing a trace with the offending packet. Or post a more detailed printout on where it's failing. Regards Anders</p></div><div id="comment-1024-info" class="comment-info"><span class="comment-age">(19 Nov '10, 10:19)</span> Anders ♦</div></div></div><div id="comment-tools-1022" class="comment-tools"></div><div class="clear"></div><div id="comment-1022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

