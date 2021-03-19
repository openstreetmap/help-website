+++
type = "question"
title = "install wireshark to SUSE Linux Enterprise Server 10 (x86_64)"
description = '''Hello, Before reading, please attention, my processor is 64-bit and so my oS is Suse_10 for 64 bit. I am trying to install wireshark on suse_10(64bit). The host does not have internet access.  Therefore, I need to have all the files needed for installation; that is even the dependencies. This is to ...'''
date = "2011-02-18T07:12:00Z"
lastmod = "2011-04-11T14:34:00Z"
weight = 2416
keywords = [ "10", "suse_10", "suse", "install", "wireshark" ]
aliases = [ "/questions/2416" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [install wireshark to SUSE Linux Enterprise Server 10 (x86\_64)](/questions/2416/install-wireshark-to-suse-linux-enterprise-server-10-x86_64)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2416-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Before reading, please attention, my processor is 64-bit and so my oS is Suse_10 for 64 bit.</p><p>I am trying to install wireshark on suse_10(64bit). The host does not have internet access. Therefore, I need to have all the files needed for installation; that is even the dependencies. This is to be able to install wireshark on a host with no internet connection. (Zypper, Yast would complain when no connection. It would try t go to net and find the dependencies.)</p><p>Currently, when I execute the rpm command like 'rpm -i wireshark-devel-1.2.8-2.8.x86_64.rpm', of course I get the errors that say, briefly, dependencies needed.</p><p>So, what I am looking for is the answer if I can make a "package" which has everything, and everything needed to be able to perform an flawless installation.</p><p>And of course, if the answer is yes, could you please tell me how?</p><p>I would really appreciate your help.</p><p>Or, a friend talked about "aptoncd". This works for ubuntu. This software can make the package I want, if I understood my friend correctly. But, what software can I use for "suse_10".</p><p>If I can find the software, I am thinking about to install a Suse_10 to my computer, and then using this program I would be able to make a package (that has everything needed in it).</p><p>Then, I would take this package to the host that I am trying to install wireshark on.</p><p>Can you please help?</p><p>thank you in advance..</p></div><div id="question-tags" class="tags-container tags">10 suse_10 suse install wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '11, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/f8deb079242bcf9cb848c2de41d36b6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudo1234&#39;s gravatar image" /><p>sudo1234<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudo1234 has no accepted answers">0%</span></p></div></div><div id="comments-container-2416" class="comments-container"></div><div id="comment-tools-2416" class="comment-tools"></div><div class="clear"></div><div id="comment-2416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3456"></span>

<div id="answer-container-3456" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3456-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Small world; I have been having trouble with the exact same issue. But in my case, I have internet access but no proper package manager. One of your options is to find a SLES iso that has a repository with a bunch of packages in it. In my case that took care of about 80% of the dependencies. The rest I had to locate and download manually. Unfortunately the install was still quite buggy and I wasn't able to successfuly compile it. =/</p><p>So in short: I haven't found a way to do it...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '11, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/e38821ea7ed026bbdf8032a0fdc64d6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tokolosh&#39;s gravatar image" /><p>Tokolosh<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tokolosh has no accepted answers">0%</span></p></div></div><div id="comments-container-3456" class="comments-container"></div><div id="comment-tools-3456" class="comment-tools"></div><div class="clear"></div><div id="comment-3456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

