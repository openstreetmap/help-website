+++
type = "question"
title = "Generate vlans file"
description = '''How can I create the vlans configuration file for use with wireshark on my mac (unix)? I do not have access to the router control panel. Thank you!'''
date = "2017-07-22T23:41:00Z"
lastmod = "2017-07-23T03:32:00Z"
weight = 63009
keywords = [ "vlan", "wlan", "file", "configuration" ]
aliases = [ "/questions/63009" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Generate vlans file](/questions/63009/generate-vlans-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63009-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I create the vlans configuration file for use with wireshark on my mac (unix)? I do not have access to the router control panel. Thank you!</p></div><div id="question-tags" class="tags-container tags">vlan wlan file configuration</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '17, 23:41</strong></p><img src="https://secure.gravatar.com/avatar/fea2009f82772ec053325ee1a66efbf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johntheone88&#39;s gravatar image" /><p>johntheone88<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johntheone88 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '17, 23:41</p></div></div><div id="comments-container-63009" class="comments-container"></div><div id="comment-tools-63009" class="comment-tools"></div><div class="clear"></div><div id="comment-63009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63010"></span>

<div id="answer-container-63010" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63010-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Start Wireshark and open the About Wireshark panel. Open the Folders tab and look for the Personal configuration line. The location on that line (\Users\[your account]\.config\wireshark) is a clickable link which opens your Finder. This is where your vlans file needs to end up.</p><p>Now create a text file according to <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChAppFilesConfigurationSection.html">the format in the users guide</a> using the TextEdit app (or some other plain text editor) and save it with the name "vlans" (no .txt) somewhere, eg. in Documents. Open another Finder, find the vlans file you just created and move it to the other Finder window.</p><p>Now go to Wireshark Preferences dialog, select the Name Resolution panel and tick the Resolve VLAN IDs checkbox, then restart Wireshark. It will load the vlans you created and add the name to the detailed 802.1Q dissection.</p><p>What names and number to add depends on the network you are connected to / view PCAP files from. Wireshark can't magically tell you which VLANs are possibly there and what their names are.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '17, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63010" class="comments-container"><span id="63025"></span><div id="comment-63025" class="comment"><div id="post-63025-score" class="comment-score"></div><div class="comment-text"><p>Thanks — my problem is how to actually <em>generate</em> the correct names for the correct ips — creating the file isn't hard, but finding out what to put in it is what I'm having trouble with, as I don't have access to the control panel. How could i find out what to put in it (like any commands I could use) I've used <code>ping</code> and that doesn't always give names</p></div><div id="comment-63025-info" class="comment-info"><span class="comment-age">(23 Jul '17, 14:32)</span> johntheone88</div></div></div><div id="comment-tools-63010" class="comment-tools"></div><div class="clear"></div><div id="comment-63010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

