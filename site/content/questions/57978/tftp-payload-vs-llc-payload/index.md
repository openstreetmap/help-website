+++
type = "question"
title = "TFTP payload vs LLC payload"
description = '''Hi, I&#x27;m working on a dissector plugin for a proprietary protocol that runs on top of Ethernet with LLC frames. My dissector is working fine, but I&#x27;m having a problem with the LLC frame when running TFTP over my protocol: Both the LLC dissector and the TFTP dissector create a &quot;data&quot; node for their pa...'''
date = "2016-12-09T06:45:00Z"
lastmod = "2016-12-10T14:35:00Z"
weight = 57978
keywords = [ "llc", "ethernet", "tftp", "filter", "display-filter" ]
aliases = [ "/questions/57978" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TFTP payload vs LLC payload](/questions/57978/tftp-payload-vs-llc-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57978-score" class="post-score" title="current number of votes">0</div><span id="post-57978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm working on a dissector plugin for a proprietary protocol that runs on top of Ethernet with LLC frames. My dissector is working fine, but I'm having a problem with the LLC frame when running TFTP over my protocol:</p><p>Both the LLC dissector and the TFTP dissector create a "data" node for their payload, and both nodes have the same attributes "len" and "data". In this setup, I can't figure out how to filter explicitly on the length of just one of the two payloads (e.g. all packets with a TFTP data length of 445, but not those with LLC data length of 445 and smaller TFTP length).</p><p>How can I uniquely address either of these nodes despite them using the same name?</p><p>Or, if that's not possible, can I somehow resolve the name clash using my custom protocol dissector that sits between the LLC and TFTP layer?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-llc" rel="tag" title="see questions tagged &#39;llc&#39;">llc</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-tftp" rel="tag" title="see questions tagged &#39;tftp&#39;">tftp</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '16, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/cfa23205cce07923a8c4e3f4b0824389?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="creckord&#39;s gravatar image" /><p><span>creckord</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="creckord has no accepted answers">0%</span></p></div></div><div id="comments-container-57978" class="comments-container"><span id="57995"></span><div id="comment-57995" class="comment"><div id="post-57995-score" class="comment-score"></div><div class="comment-text"><p>The LLC dissector only creates a "data" node if its payload isn't dissected. However, if your dissector runs on top of LLC, presumably the LLC dissector is calling your dissector to dissect the payload, so there shouldn't <em>be</em> a "data" node.</p><p>Does your protocol have a particular DSAP assigned to it, or does it run on top of SNAP?</p></div><div id="comment-57995-info" class="comment-info"><span class="comment-age">(10 Dec '16, 14:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-57978" class="comment-tools"></div><div class="clear"></div><div id="comment-57978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

