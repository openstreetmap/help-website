+++
type = "question"
title = "How to parse a String hex text"
description = '''I have a packet (hex string) which I have framed programmatically. Need to Parse the hex String to display the human readable form. What command should I use to Parse the HexString. I am looking for a command line interface solution.  Thanks, Chetan'''
date = "2016-09-22T06:14:00Z"
lastmod = "2016-09-22T06:14:00Z"
weight = 55751
keywords = [ "parse", "parser", "command-line" ]
aliases = [ "/questions/55751" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to parse a String hex text](/questions/55751/how-to-parse-a-string-hex-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55751-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a packet (hex string) which I have framed programmatically. Need to Parse the hex String to display the human readable form. What command should I use to Parse the HexString. I am looking for a command line interface solution. Thanks, Chetan</p></div><div id="question-tags" class="tags-container tags">parse parser command-line</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '16, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/13c01090e672eed966eb0deac4a1abf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chetan%20Ragi&#39;s gravatar image" /><p>Chetan Ragi<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chetan Ragi has no accepted answers">0%</span></p></div></div><div id="comments-container-55751" class="comments-container"><span id="55753"></span><div id="comment-55753" class="comment"><div id="post-55753-score" class="comment-score"></div><div class="comment-text"><p>Do I get you right that you have assembled a packet of some protocol, but instead of saving it as binary data, you've printed it out as hex string, and you want to dissect it using Wireshark? If this is the case, then there is the "import from hex dump" functionality of Wireshark in the File menu.</p><p>You have to print the hex data in the following form:</p><p><code>000000  ab cd ef</code></p><p>where <code>000000</code> is an offset and <code>ab cd ef</code> are the actual data.</p><p>You also need to tell Wireshark which is the lowest layer in those data (Ethernet, IP or possibly some other one) by choosing the proper encapsulation from the drop-down list.</p></div><div id="comment-55753-info" class="comment-info"><span class="comment-age">(22 Sep '16, 07:37)</span> sindy</div></div></div><div id="comment-tools-55751" class="comment-tools"></div><div class="clear"></div><div id="comment-55751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

