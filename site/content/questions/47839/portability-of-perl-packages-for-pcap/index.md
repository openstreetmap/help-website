+++
type = "question"
title = "portability of perl packages for pcap"
description = '''Kurt gave an interesting perl script to check if a blacklisted IP addresses appeared in a pcap file. I love perl but not sure if the packages such as Net::Pcap is ported to cygwin.'''
date = "2015-11-21T09:13:00Z"
lastmod = "2015-11-21T11:21:00Z"
weight = 47839
keywords = [ "libpcap" ]
aliases = [ "/questions/47839" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [portability of perl packages for pcap](/questions/47839/portability-of-perl-packages-for-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47839-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Kurt gave an interesting perl <a href="https://ask.wireshark.org/questions/45344/is-it-possible-to-use-a-blacklisttxt-file-as-an-input-list-for-a-wireshark-tshark-displayfilter">script</a> to check if a blacklisted IP addresses appeared in a pcap file. I love perl but not sure if the packages such as Net::Pcap is ported to cygwin.</p></div><div id="question-tags" class="tags-container tags">libpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '15, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-47839" class="comments-container"></div><div id="comment-tools-47839" class="comment-tools"></div><div class="clear"></div><div id="comment-47839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47841"></span>

<div id="answer-container-47841" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47841-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On Windows you can use <a href="http://www.activestate.com/activeperl">ActiveState Perl</a>, which contains Net::Pcap, or at least you can easily install it with ppm (<code>ppm install Net::Pcap</code>).</p><p>I tested <a href="https://ask.wireshark.org/questions/45344/is-it-possible-to-use-a-blacklisttxt-file-as-an-input-list-for-a-wireshark-tshark-displayfilter/45506">my example</a> with ActivePerl on Windows :-)</p><p>BTW: You can try to install Net::Pcap for Cygwin as well, but it seems to be quite some work.</p><blockquote><p><a href="http://use.perl.org/use.perl.org/_somian/journal/27529.html">http://use.perl.org/use.perl.org/_somian/journal/27529.html</a><br />
</p></blockquote><p>I can't help you with that, as I'm not using Cygwin.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '15, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Nov '15, 11:25</p></div></div><div id="comments-container-47841" class="comments-container"><span id="47867"></span><div id="comment-47867" class="comment"><div id="post-47867-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer, it appears that ActiveState perl doesn't have the support any more: <code>C:\Perl64\bin&gt;ppm install Net::Pcap Downloading ActiveState Package Repository packlist...done Updating ActiveState Package Repository database...done ppm install failed: Can't find any package that provides Net::Pcap</code>. I am using ActiveState perl 5.14.2 on Win7.</p></div><div id="comment-47867-info" class="comment-info"><span class="comment-age">(23 Nov '15, 07:36)</span> pktUser1001</div></div><span id="47869"></span><div id="comment-47869" class="comment"><div id="post-47869-score" class="comment-score"></div><div class="comment-text"><p>I run 5.16.3 and it's there, however I do have the 32-bit version. Maybe they don't offer a 64-bit version of Net::Pcap. Please try the 32-bit version of Perl.</p></div><div id="comment-47869-info" class="comment-info"><span class="comment-age">(23 Nov '15, 08:26)</span> Kurt Knochner ♦</div></div><span id="47878"></span><div id="comment-47878" class="comment"><div id="post-47878-score" class="comment-score"></div><div class="comment-text"><pre><code>perl -v

This is perl 5, version 16, subversion 3 (v5.16.3) built for MSWin32-x86-multi-thread
(with 1 registered patch, see perl -V for more detail)

Copyright 1987-2012, Larry Wall

Binary build 1604 [298023] provided by ActiveState http://www.ActiveState.com
Built Apr 14 2014 14:32:20

Perl may be copied only under the terms of either the Artistic License or the
GNU General Public License, which may be found in the Perl 5 source kit.

Complete documentation for Perl, including FAQ lists, should be found on
this system using &quot;man perl&quot; or &quot;perldoc perl&quot;.  If you have access to the
Internet, point your browser at http://www.perl.org/, the Perl Home Page.
</code></pre><pre><code>perl  -e &quot;use Net::Pcap; print $Net::Pcap::VERSION&quot;
0.17</code></pre></div><div id="comment-47878-info" class="comment-info"><span class="comment-age">(23 Nov '15, 11:12)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-47841" class="comment-tools"></div><div class="clear"></div><div id="comment-47841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

