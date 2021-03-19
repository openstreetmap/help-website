+++
type = "question"
title = "Can I change data in other frames from the current frame in a dissector?"
description = '''I know that dissectors only work on the current packet, but is there a way to access previous or future frames from the current frame in a dissector? I am trying to display a calculated checksum in the initial frame after the whole fragmented message has been reassembled.'''
date = "2017-06-08T10:49:00Z"
lastmod = "2017-06-08T14:36:00Z"
weight = 61873
keywords = [ "reassembly", "frame", "dissector", "reassemble", "checksum" ]
aliases = [ "/questions/61873" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I change data in other frames from the current frame in a dissector?](/questions/61873/can-i-change-data-in-other-frames-from-the-current-frame-in-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61873-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know that dissectors only work on the current packet, but is there a way to access previous or future frames from the current frame in a dissector? I am trying to display a calculated checksum in the initial frame after the whole fragmented message has been reassembled.</p></div><div id="question-tags" class="tags-container tags">reassembly frame dissector reassemble checksum</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '17, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/ec69e82648ca5a020df1522509212989?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jpetersen&#39;s gravatar image" /><p>jpetersen<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jpetersen has no accepted answers">0%</span></p></div></div><div id="comments-container-61873" class="comments-container"><span id="61875"></span><div id="comment-61875" class="comment"><div id="post-61875-score" class="comment-score"></div><div class="comment-text"><p>Shouldn't you be doing that in the last frame together with the Reassembled data?</p></div><div id="comment-61875-info" class="comment-info"><span class="comment-age">(08 Jun '17, 11:55)</span> Anders ♦</div></div><span id="61877"></span><div id="comment-61877" class="comment"><div id="post-61877-score" class="comment-score"></div><div class="comment-text"><p>I would like to display it in the initial fragment as well because that has all of the other information from the message in it.</p><p>I want to display all the information with the validated checksum so either add the calculated checksum to a previous frame, or add all the information from the initial fragment to the future frame where the checksum is calculated.</p></div><div id="comment-61877-info" class="comment-info"><span class="comment-age">(08 Jun '17, 13:04)</span> jpetersen</div></div></div><div id="comment-tools-61873" class="comment-tools"></div><div class="clear"></div><div id="comment-61873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61881"></span>

<div id="answer-container-61881" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61881-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is possible taking into account how Wireshark is processing your capture file. First it reads it sequentially and then uses additional, random access reads to get details.</p><p>You can make use of that, eg. for request and response tracking. This is described in <code>doc/README.request_response_tracking</code>. You can track other stuff as well, eg. the data you seem to need.</p><p>Mind you this depends on 2-pass analysis of the capture file, so it using tshark you'll have to give the <code>-2</code> option for it to work there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '17, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61881" class="comments-container"><span id="61911"></span><div id="comment-61911" class="comment"><div id="post-61911-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply, I have been looking into request_response_tracking and it has been helpful.</p></div><div id="comment-61911-info" class="comment-info"><span class="comment-age">(09 Jun '17, 08:47)</span> jpetersen</div></div></div><div id="comment-tools-61881" class="comment-tools"></div><div class="clear"></div><div id="comment-61881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

