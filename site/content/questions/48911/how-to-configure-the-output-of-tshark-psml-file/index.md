+++
type = "question"
title = "How to configure the output of Tshark .psml file"
description = '''I am creating a simple packet analyzer in Python in which analyzes Tshark .xml output files. Tshark (command line equivalent of Wireshark) has a feature which allows to output all the packets to the .psml file (Packet Summary Markup Language). In Wireshark I can configure the contents of the exporte...'''
date = "2016-01-06T07:46:00Z"
lastmod = "2016-01-09T12:03:00Z"
weight = 48911
keywords = [ "xml", "wlan", "wifi", "psml", "tshark" ]
aliases = [ "/questions/48911" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to configure the output of Tshark .psml file](/questions/48911/how-to-configure-the-output-of-tshark-psml-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48911-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am creating a simple packet analyzer in Python in which analyzes Tshark <code>.xml</code> output files.</p><p>Tshark (command line equivalent of Wireshark) has a feature which allows to output all the packets to the .psml file (Packet Summary Markup Language). In Wireshark I can configure the contents of the exported .psml file by adding/removing tabs in the GUI. However, I can't find any option to do this by using a command line in Tshark.</p><p>Sample output from Wireshark:</p><pre><code>&lt;?xml version=&quot;1.0&quot;?&gt;
&lt;psml version=&quot;0&quot; creator=&quot;wireshark/2.0.0&quot;&gt;
&lt;structure&gt;
&lt;section&gt;No.&lt;/section&gt;
&lt;section&gt;Time&lt;/section&gt;
&lt;section&gt;Source&lt;/section&gt;
&lt;section&gt;Destination&lt;/section&gt;
&lt;section&gt;Protocol&lt;/section&gt;
&lt;section&gt;Length&lt;/section&gt;
&lt;section&gt;Info&lt;/section&gt;
&lt;section&gt;dBm&lt;/section&gt;
&lt;/structure&gt;

&lt;packet&gt;
&lt;section&gt;1&lt;/section&gt;
&lt;section&gt;0.000000&lt;/section&gt;
&lt;section&gt;xx:xx:xx:xx:xx:xx&lt;/section&gt;
&lt;section&gt;Broadcast&lt;/section&gt;
&lt;section&gt;802.11&lt;/section&gt;
&lt;section&gt;223&lt;/section&gt;
&lt;section&gt;Beacon frame, SN=1524, FN=0, Flags=........C, BI=100, SSID=xxx&lt;/section&gt;
&lt;section&gt;4294967260 dBm&lt;/section&gt;
&lt;/packet&gt;</code></pre><p>In Tshark I am getting the output without the section dBm (IEEE 802.11 RSSI). How to configure Tshark to get this data in <code>.psml</code> file?</p></div><div id="question-tags" class="tags-container tags">xml wlan wifi psml tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '16, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/51312cb4f8c7722a8b3a6b91d3e1f34e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="6franek&#39;s gravatar image" /><p>6franek<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="6franek has no accepted answers">0%</span></p></div></div><div id="comments-container-48911" class="comments-container"></div><div id="comment-tools-48911" class="comment-tools"></div><div class="clear"></div><div id="comment-48911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49021"></span>

<div id="answer-container-49021" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49021-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark is using the same fields/columns that Wireshark is using in the default (current) profile. So if you want to change the output of tshark PSML, you can do one of the following things.</p><ul><li>modify the columns in Wireshark and save the profile</li><li>edit the preferences file directly (<strong>%APPDATA%/Wireshark/preferences</strong> - entry: <strong>gui.column.format:</strong>)</li><li>use tsharks column format (see <strong>tshark -G column-formats</strong>)</li></ul><p>An alternative would be to use PDML (-T pdml), which is much more 'chatty', meaning it prints more (is not all) fields or <strong>tshark -V</strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '16, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-49021" class="comments-container"></div><div id="comment-tools-49021" class="comment-tools"></div><div class="clear"></div><div id="comment-49021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

