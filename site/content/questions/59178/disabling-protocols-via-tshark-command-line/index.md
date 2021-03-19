+++
type = "question"
title = "Disabling protocols via tshark command line"
description = '''I am using tshark with matlab so that we can analyze the data in matlab. I recently had a problem where a UDP &quot;blob&quot; message was being decoded as an GVSP message, and in some instances the Field &quot;data&quot; was not being returned in the tshark decode. I eventually discovered that if I turned off the GVSP...'''
date = "2017-01-31T06:13:00Z"
lastmod = "2017-01-31T07:50:00Z"
weight = 59178
keywords = [ "decode", "udp", "tshark" ]
aliases = [ "/questions/59178" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Disabling protocols via tshark command line](/questions/59178/disabling-protocols-via-tshark-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59178-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using tshark with matlab so that we can analyze the data in matlab. I recently had a problem where a UDP "blob" message was being decoded as an GVSP message, and in some instances the Field "data" was not being returned in the tshark decode. I eventually discovered that if I turned off the GVSP protocol in wireshark that the tshark decoding then worked.<br />
</p><p>Since I deliver the matlab that calls the tshark to "clients", it would be nice if I didn't have to also tell them to disable GVSP. I also deliver this to clients on both Linux and windows who may have totally different versions of wire shark installed, so to build a configuration that has GVSP disabled would be problematic.</p><p>So to get to the question is there a way that I can just define on the command line that I want all UDP messages to be decoded as UDP and nothing else?</p><p>Thanks Mark</p></div><div id="question-tags" class="tags-container tags">decode udp tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '17, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/1009ea8b551c942cb060d74bc7cbe8f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschek&#39;s gravatar image" /><p>petschek<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschek has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-59178" class="comments-container"></div><div id="comment-tools-59178" class="comment-tools"></div><div class="clear"></div><div id="comment-59178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59181"></span>

<div id="answer-container-59181" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59181-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the <a href="https://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code></a> man page:</p><pre><code>--disable-protocol &lt;proto_name&gt;

    Disable dissection of proto_name.</code></pre><p>If the version of Wireshark is too old and doesn't support this option, you could add <code>gvsp</code> to the <code>disabled_protos</code> file located in the Wireshark <em>"Personal configuration"</em> folder.</p><p>But since that changes the users' configuration, perhaps a better alternative is for you to create a separate <em>"matlab"</em> Wireshark <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChCustConfigProfilesSection.html">profile</a> and ask your users to copy it to their <em>"Personal configuration"</em> profiles directory, which would only need to be done once. That profile could disable all protocols except for only those that you want enabled. After that, you can just run <code>tshark</code> with the <code>[ -C configuration profile ]</code> option. All other profiles would be unaffected.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '17, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59181" class="comments-container"></div><div id="comment-tools-59181" class="comment-tools"></div><div class="clear"></div><div id="comment-59181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

