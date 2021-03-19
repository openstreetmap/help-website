+++
type = "question"
title = "Localized LUA Dissector tostring() in TShark Output"
description = '''I have a bunch of Wireshark LUA dissectors which populate tree contents by using LUAs tostring() method. There are places where I output double with tostring(). Now tostring() seems to use some kind of locale to determine the decimal splitter to use for doubles. On my windows host machine, which is ...'''
date = "2017-04-19T14:45:00Z"
lastmod = "2017-04-19T14:45:00Z"
weight = 60902
keywords = [ "locale", "lua", "dissector", "tostring", "tshark" ]
aliases = [ "/questions/60902" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Localized LUA Dissector tostring() in TShark Output](/questions/60902/localized-lua-dissector-tostring-in-tshark-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60902-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a bunch of Wireshark LUA dissectors which populate tree contents by using LUAs tostring() method. There are places where I output double with tostring(). Now tostring() seems to use some kind of locale to determine the decimal splitter to use for doubles. On my windows host machine, which is german, I get commas in TSharks output and in a linux guest machine I get dots in TSharks output for doubles. Obviously because of the locale.</p><p>Now my thought was that I just have to change Wiresharks/TSharks locale/language. From the Wireshark UI this is no problem (Edit &gt; Settings bla bla ...) but I'm unable to set the locale for TShark by e. g. using the following command line "$ tshark -o language:??? ...". TShark throws an error which states that the flag "language" is unknown. I even can't find a corresponding setting by calling "$ tshark -G currentprefs".</p><p>Is it even possible to set TSharks locale by command line and when... how?</p></div><div id="question-tags" class="tags-container tags">locale lua dissector tostring tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '17, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/9d7dbf758c1141692cc3171d5bf6296b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="3idet&#39;s gravatar image" /><p>3idet<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="3idet has no accepted answers">0%</span></p></div></div><div id="comments-container-60902" class="comments-container"></div><div id="comment-tools-60902" class="comment-tools"></div><div class="clear"></div><div id="comment-60902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

