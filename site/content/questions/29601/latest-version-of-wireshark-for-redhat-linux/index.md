+++
type = "question"
title = "latest version of wireshark for redhat linux"
description = '''when i check for the latest version of wireshark in my redhad linux(Red Hat Enterprise Linux Server release 6.2 (Santiago)) system it showed me this yum list wireshark* wireshark.x86_64 1.2.15-2.el6_2.1 @rhel-x86_64-server-6.4.z  wireshark.i686 1.2.15-2.el6_2.1 rhel-x86_64-server-6.4.z  wireshark-de...'''
date = "2014-02-10T01:36:00Z"
lastmod = "2014-02-10T05:28:00Z"
weight = 29601
keywords = [ "install", "linux" ]
aliases = [ "/questions/29601" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [latest version of wireshark for redhat linux](/questions/29601/latest-version-of-wireshark-for-redhat-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29601-score" class="post-score" title="current number of votes">0</div><span id="post-29601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when i check for the latest version of wireshark in my redhad linux(Red Hat Enterprise Linux Server release 6.2 (Santiago)) system it showed me this yum list wireshark*</p><p>wireshark.x86_64 1.2.15-2.el6_2.1 @rhel-x86_64-server-6.4.z wireshark.i686 1.2.15-2.el6_2.1 rhel-x86_64-server-6.4.z<br />
wireshark-devel.i686 1.2.15-2.el6_2.1 rhel-x86_64-server-optional-6.4.z wireshark-devel.x86_64 1.2.15-2.el6_2.1 rhel-x86_64-server-optional-6.4.z wireshark-gnome.x86_64 1.2.15-2.el6_2.1 rhel-x86_64-server-6.4.z<br />
</p><p>but on the web site it shows 1.10.5 as the latest stable build</p><p>how do i installed the latest stable version of wireshark in redhad linux. please provide details on how to do this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '14, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/be8a9b2e9d87b13606c3b9e75d26e71d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scara&#39;s gravatar image" /><p><span>scara</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scara has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Feb '14, 02:25</strong> </span></p></div></div><div id="comments-container-29601" class="comments-container"></div><div id="comment-tools-29601" class="comment-tools"></div><div class="clear"></div><div id="comment-29601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29622"></span>

<div id="answer-container-29622" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29622-score" class="post-score" title="current number of votes">1</div><span id="post-29622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but on the web site it shows 1.10.5 as the latest stable build</p></blockquote><p>yes, that's because RedHat does not update its Wireshark package. Please ask them why, or even better 'demand' a newer package if you own a valid support contract! If enough people start complaining they might change their mind about their Wireshark release/packaging policy ;-)</p><blockquote><p>how do i installed the latest stable version of wireshark in redhad linux. please provide details on how to do this.</p></blockquote><p>Well, these are your options</p><ul><li>compile it yourself from the sources: <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallUnixBuild.html">http://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallUnixBuild.html</a> . <strong>However</strong> you need a solid understanding how the build tools work, it there are any dependencies missing on your system. So, this is something for the experienced Linux guys.</li><li>Use RedHat only to capture the traffic with <strong>tcpdump</strong> or <strong>dumpcap</strong>. Then use another system (real or virtual machine) to analyze the capture file with the latest Wireshark release on Windows, Linux (almost all distributions contain a newer release than RedHat), Mac OS X or whatever is best for you.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29622" class="comments-container"></div><div id="comment-tools-29622" class="comment-tools"></div><div class="clear"></div><div id="comment-29622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

