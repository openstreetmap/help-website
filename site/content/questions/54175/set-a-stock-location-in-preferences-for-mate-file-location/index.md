+++
type = "question"
title = "Set a stock location in preferences for mate file location"
description = '''Hi guys I&#x27;m trying to set the stock location for my mate file to be the Roaming&#92;Wireshark folder # The name of the file containing the mate module&#x27;s configuration # A path to a file mate.config: %APPDATA%&#92;Wireshark&#92;quantel.mate  Is there a specific location I should be setting, as nothing I try seem...'''
date = "2016-07-19T21:52:00Z"
lastmod = "2016-07-19T21:52:00Z"
weight = 54175
keywords = [ "installer", "preferences", "wireshark" ]
aliases = [ "/questions/54175" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Set a stock location in preferences for mate file location](/questions/54175/set-a-stock-location-in-preferences-for-mate-file-location)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54175-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys I'm trying to set the stock location for my mate file to be the Roaming\Wireshark folder</p><pre><code># The name of the file containing the mate module&#39;s configuration
# A path to a file
mate.config: %APPDATA%\Wireshark\quantel.mate</code></pre><p>Is there a specific location I should be setting, as nothing I try seems to work.<br />
I'd like to make it as generic as possible so customers and staff can use some predefined filters without too much messing about Any thoughts on how I can add a generic path to roaming\wireshark? I would have thought this would work.</p><p>Cheers Scott</p></div><div id="question-tags" class="tags-container tags">installer preferences wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '16, 21:52</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p>Scott Harman<br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span> </br></p></div></div><div id="comments-container-54175" class="comments-container"><span id="54210"></span><div id="comment-54210" class="comment"><div id="post-54210-score" class="comment-score"></div><div class="comment-text"><p>What happens when it doesn't work? Do users get an error indicating that MATE can't find the MATE configuration file or does the preference not apply (e.g., if they look in the MATE preference they see an empty file name)?</p><p>If it's the former then are you sure the file is there on their system? I wasn't sure variable (<code>%APPDATA%</code>) would work in the file name but it seems to here.</p><p>If it's the latter, where, exactly, are you placing this global preferences file (what's the full path name) and where does Help-&gt;About-&gt;Folders say Global configuration files go? Can you change other preferences via this global preference file?</p></div><div id="comment-54210-info" class="comment-info"><span class="comment-age">(20 Jul '16, 14:23)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-54175" class="comment-tools"></div><div class="clear"></div><div id="comment-54175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

