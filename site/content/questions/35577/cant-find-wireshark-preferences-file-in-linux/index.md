+++
type = "question"
title = "Can&#x27;t Find Wireshark preferences file in Linux"
description = '''I know how to access the preferences for wireshark from the preferences under edit menu . But I want to access the corresponding file to them. Based on my understanding for what is in the Wireshark User&#x27;s Guide, It is supposed to be in /etc/wireshark.conf or $HOME/.wireshark/preferences. However, I&#x27;...'''
date = "2014-08-19T07:05:00Z"
lastmod = "2014-08-19T07:34:00Z"
weight = 35577
keywords = [ "linux", "preferences", "file", "wireshark" ]
aliases = [ "/questions/35577" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can't Find Wireshark preferences file in Linux](/questions/35577/cant-find-wireshark-preferences-file-in-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35577-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know how to access the preferences for wireshark from the preferences under edit menu . But I want to access the corresponding file to them. Based on my understanding for what is in the Wireshark User's Guide, It is supposed to be in /etc/wireshark.conf or $HOME/.wireshark/preferences. However, I'm not able to find it in there!</p><p>My questions why I don't have the "preferences" file in any one of these two places? where can I find it instead?</p><p>Note: I've installed Wireshark latest released version from source.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">linux preferences file wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-35577" class="comments-container"></div><div id="comment-tools-35577" class="comment-tools"></div><div class="clear"></div><div id="comment-35577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35578"></span>

<div id="answer-container-35578" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35578-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the Wireshark application menu: Help | About Wireshark, select the Folders tab and you should see the paths to the Personal and Global configuration directories.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '14, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35578" class="comments-container"><span id="35582"></span><div id="comment-35582" class="comment"><div id="post-35582-score" class="comment-score"></div><div class="comment-text"><p>This doesn't work for me too. I've got the error message: "Failed to open "/home/flora/.wireshark". Error when getting information for file '/home/flora/.wireshark': No such file or directory."</p></div><div id="comment-35582-info" class="comment-info"><span class="comment-age">(19 Aug '14, 09:19)</span> flora</div></div><span id="35583"></span><div id="comment-35583" class="comment"><div id="post-35583-score" class="comment-score"></div><div class="comment-text"><p>That would suggest the wireshark executable doesn't have the required privileges to open that directory.</p><p>Odd, and unfortunately now out of my realm of competence.</p></div><div id="comment-35583-info" class="comment-info"><span class="comment-age">(19 Aug '14, 09:28)</span> grahamb ♦</div></div><span id="35599"></span><div id="comment-35599" class="comment"><div id="post-35599-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb. It seems it does because When I do, ls -l /usr/local/bin/wireshark I get: -rwxr-xr-x 1 root root 8687638 Aug 18 17:18 /usr/local/bin/wireshark</p><p>I only can find 'recent' and 'recent_common' but not 'preferences' file</p></div><div id="comment-35599-info" class="comment-info"><span class="comment-age">(19 Aug '14, 15:45)</span> flora</div></div><span id="35605"></span><div id="comment-35605" class="comment"><div id="post-35605-score" class="comment-score"></div><div class="comment-text"><p>Try modifying the preferences in Wireshark and clicking OK. That may then save a new preferences file.</p></div><div id="comment-35605-info" class="comment-info"><span class="comment-age">(20 Aug '14, 01:23)</span> grahamb ♦</div></div><span id="35625"></span><div id="comment-35625" class="comment"><div id="post-35625-score" class="comment-score"></div><div class="comment-text"><p>What user are you running Wirshark as? What are the permissions on /home/flora/ and /home/flora/.wireshark/ ?</p></div><div id="comment-35625-info" class="comment-info"><span class="comment-age">(20 Aug '14, 07:08)</span> JeffMorriss ♦</div></div><span id="35738"></span><div id="comment-35738" class="comment not_top_scorer"><div id="post-35738-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb and JeffMorriss! the problem has solved itself somehow. I'm not really aware how as all what I did is rebuild wireshark again and I found the 'preferences' file along with 'recent' and 'recent_common' files.</p></div><div id="comment-35738-info" class="comment-info"><span class="comment-age">(25 Aug '14, 16:56)</span> flora</div></div></div><div id="comment-tools-35578" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-35578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

