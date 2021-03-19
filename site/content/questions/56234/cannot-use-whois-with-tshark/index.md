+++
type = "question"
title = "Cannot use `whois` with `tshark`"
description = '''I am unable to get the orgname or whois output with tshark.  The commands  tshark -lq -T fields -e whois.answer tshark -lq -T fields -e ip.geoip.src_org  Give me a empty lines. Why is it so?'''
date = "2016-10-08T10:03:00Z"
lastmod = "2016-10-09T04:30:00Z"
weight = 56234
keywords = [ "geolocalization", "whois", "geo-ip" ]
aliases = [ "/questions/56234" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot use \`whois\` with \`tshark\`](/questions/56234/cannot-use-whois-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56234-score" class="post-score" title="current number of votes">0</div><span id="post-56234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am unable to get the orgname or whois output with <code>tshark</code>.</p><p>The commands</p><ol><li><code>tshark -lq -T fields -e whois.answer</code></li><li><code>tshark -lq -T fields -e ip.geoip.src_org</code></li></ol><p>Give me a empty lines.</p><p>Why is it so?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-geolocalization" rel="tag" title="see questions tagged &#39;geolocalization&#39;">geolocalization</span> <span class="post-tag tag-link-whois" rel="tag" title="see questions tagged &#39;whois&#39;">whois</span> <span class="post-tag tag-link-geo-ip" rel="tag" title="see questions tagged &#39;geo-ip&#39;">geo-ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '16, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/1d0a5c898c23c1ae1a7b009804920031?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user31415&#39;s gravatar image" /><p><span>user31415</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user31415 has no accepted answers">0%</span></p></div></div><div id="comments-container-56234" class="comments-container"><span id="56236"></span><div id="comment-56236" class="comment"><div id="post-56236-score" class="comment-score"></div><div class="comment-text"><p>Are you attempting to run tshark on a previous capture or a live capture as you don't seem to be providing either a file to read or an interface to capture on? By default, with no file or interface specified, tshark will attempt to capture on some interface which may not be what you intend.</p><p>In either case, are you sure the file or live capture traffic contains the fields of interest?</p></div><div id="comment-56236-info" class="comment-info"><span class="comment-age">(08 Oct '16, 10:46)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56246"></span><div id="comment-56246" class="comment"><div id="post-56246-score" class="comment-score"></div><div class="comment-text"><p>Can you provide an example that works for you? I tried <code>tshark -i wlp3s0 -lq -T fields -e ip.dst -w output</code> then <code>tshark -lq -T fields -e whois.answer -r output</code>. I only have blank lines. Same thing for any <code>whois</code> fields listed in <code>tshark -G</code>.</p></div><div id="comment-56246-info" class="comment-info"><span class="comment-age">(09 Oct '16, 03:26)</span> <span class="comment-user userinfo">user31415</span></div></div><span id="56247"></span><div id="comment-56247" class="comment"><div id="post-56247-score" class="comment-score"></div><div class="comment-text"><p>It can also be linked to my OS, I am using <code>Ubuntu 16.04</code></p></div><div id="comment-56247-info" class="comment-info"><span class="comment-age">(09 Oct '16, 03:33)</span> <span class="comment-user userinfo">user31415</span></div></div><span id="56251"></span><div id="comment-56251" class="comment"><div id="post-56251-score" class="comment-score"></div><div class="comment-text"><p>Are you sure you have whois traffic in your capture? If I capture whois traffic then the field <code>whois.answer</code> produces the expected results.</p><p>To get results from the ip.geoip.src_org field you must also have configured up geoip lookups in the Wireshark preferences (i.e. downloaded a database).</p><p>Try loading your capture in Wireshark and using a display filter of "whois" to see if you do have whois traffic.</p></div><div id="comment-56251-info" class="comment-info"><span class="comment-age">(09 Oct '16, 04:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56234" class="comment-tools"></div><div class="clear"></div><div id="comment-56234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

