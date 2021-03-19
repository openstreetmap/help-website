+++
type = "question"
title = "What is the IP header checksum used for and how to calculate it?"
description = '''Solved I have a udp packet captured through multicast channel and I found that there is a Header checksum under Internet Protocol Version 4.  I would like to ask  What is it used for? How to calculate it?  I have tried to search on the web but what I found is the check sum calculation for the whole ...'''
date = "2017-10-22T03:00:00Z"
lastmod = "2017-10-22T07:08:00Z"
weight = 64084
keywords = [ "ip", "checksum", "calculate", "header" ]
aliases = [ "/questions/64084" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is the IP header checksum used for and how to calculate it?](/questions/64084/what-is-the-ip-header-checksum-used-for-and-how-to-calculate-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64084-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>Solved</strong><br />
I have a udp packet captured through multicast channel and I found that there is a <em>Header checksum</em> under <em>Internet Protocol Version 4</em>.<br />
<img src="https://osqa-ask.wireshark.org/upfiles/temp_oDAS9cc.png" alt="alt text" /></p><p>I would like to ask</p><ol><li>What is it used for?</li><li>How to calculate it?</li></ol><p>I have tried to search on the web but what I found is the check sum calculation for the whole UDP packet which seems not the same checksum that I am asking for on the above.</p><p>Here is what I do for IP Header checksum:</p><pre><code>void ReCalculateCheckSum_IPHeader(u_char* pData)
{
    // reset checksum
    pData[24] = 0;
    pData[25] = 0;

    uint32_t unChecksum = 0;
    const uint16_t* pD16;
    pD16 = reinterpret_cast&lt;const uint16_t*&gt;(pData + CommonHelper::IP_HEADER_OFFSET);

    // adding checksum for scr IP and dst IP
    for (int i = 0; i &lt; 10; i++)
    {
        unChecksum += _byteswap_ushort(*pD16++);
    }
    while (unChecksum &gt;&gt; 16)
    {
        unChecksum = (unChecksum &amp; 0xffff) + (unChecksum &gt;&gt; 16);
    }

    // set checksum back to data
    uint16_t un16TempChecksum = static_cast&lt;uint16_t&gt;(~unChecksum);
    un16TempChecksum = _byteswap_ushort(un16TempChecksum);
    memcpy((char*)(pData + 24), &amp;un16TempChecksum, sizeof(uint16_t));
}</code></pre><p>Here is what I do for the UDP checksum:</p><pre><code>void ReCalculateCheckSum_UDP_Pkt(u_char* pData, unsigned int unDataLen)
{
    // reset checksum
    pData[40] = 0;
    pData[41] = 0;

    uint32_t unChecksum = 0;
    const uint16_t* pD16;
    const uint8_t* pD8;
    // handle IP layer
    //      handle src IP
    pD16 = reinterpret_cast&lt;const uint16_t*&gt;(pData + 26);
    unChecksum += _byteswap_ushort(*pD16++); // since wireshark file is big-endian, but c++ in PC is little-endian
    unChecksum += _byteswap_ushort(*pD16);
    //      handle dst IP
    pD16 = reinterpret_cast&lt;const uint16_t*&gt;(pData + 30);
    unChecksum += _byteswap_ushort(*pD16++); // since wireshark file is big-endian, but c++ in PC is little-endian
    unChecksum += _byteswap_ushort(*pD16);
    //      handle portocol
    pD8 = reinterpret_cast&lt;const uint8_t*&gt;(pData + 23);
    unChecksum += *pD8;
    //      handle data lenght, from IP layer to udp data layer
    pD16 = reinterpret_cast&lt;const uint16_t*&gt;(pData + 38);
    unChecksum += _byteswap_ushort(*pD16);


    // handle UDP layer
    //      handle src Port
    pD16 = reinterpret_cast&lt;const uint16_t*&gt;(pData + 34);
    unChecksum += _byteswap_ushort(*pD16);
    //      handle dst Port
    pD16 = reinterpret_cast&lt;const uint16_t*&gt;(pData + 36);
    unChecksum += _byteswap_ushort(*pD16);
    //      handle data lenght, from IP layer to udp data layer
    pD16 = reinterpret_cast&lt;const uint16_t*&gt;(pData + 38);
    unChecksum += _byteswap_ushort(*pD16);

    // handle udp data
    size_t len = unDataLen - CommonHelper::DATAGRAME_DATA_OFFSET; // 42 is the Ethernet header
    pD16 = reinterpret_cast&lt;const uint16_t*&gt;(pData + CommonHelper::DATAGRAME_DATA_OFFSET);
    while (len &gt; 1)
    {
        unChecksum += _byteswap_ushort(*pD16++); // since wireshark file is big-endian, but c++ in PC is little-endian
        len -= sizeof(uint16_t);
    }
    if (len) // if total lenght the data is odd
    {
        unChecksum += *reinterpret_cast&lt;const uint8_t*&gt;(pD16);
    }


    while (unChecksum &gt;&gt; 16)
    {
        unChecksum = (unChecksum &amp; 0xffff) + (unChecksum &gt;&gt; 16);
    }

    // set checksum back to data
    uint16_t un16TempChecksum = static_cast&lt;uint16_t&gt;(~unChecksum);
    un16TempChecksum = _byteswap_ushort(un16TempChecksum);
    memcpy((char*)(pData + 40), &amp;un16TempChecksum, sizeof(uint16_t));
}</code></pre></div><div id="question-tags" class="tags-container tags">ip checksum calculate header</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '17, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/7c0faeca14601a7e181f27988b503982?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SulfredLee&#39;s gravatar image" /><p>SulfredLee<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SulfredLee has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Oct '17, 06:12</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-64084" class="comments-container"></div><div id="comment-tools-64084" class="comment-tools"></div><div class="clear"></div><div id="comment-64084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="64085"></span>

<div id="answer-container-64085" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64085-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The picture shows the IP header and its header checksum. The IP header checksum is used to protect it against errors, same as all the other checksums in a packet for their various parts.</p><p>Here's one example of how to calculate it: <a href="http://www.thegeekstuff.com/2012/05/ip-header-checksum/">http://www.thegeekstuff.com/2012/05/ip-header-checksum/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '17, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-64085" class="comments-container"><span id="64087"></span><div id="comment-64087" class="comment"><div id="post-64087-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much. It works.</p></div><div id="comment-64087-info" class="comment-info"><span class="comment-age">(22 Oct '17, 05:30)</span> SulfredLee</div></div></div><div id="comment-tools-64085" class="comment-tools"></div><div class="clear"></div><div id="comment-64085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="64091"></span>

<div id="answer-container-64091" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64091-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To be clear, the IP Header Checksum helps protect against errors in the IP header <em>only</em>, and not with errors in the payload. This is by design. For further reading, refer to <a href="https://tools.ietf.org/html/rfc791">RFC 791</a> <code>INTERNET PROTOCOL</code>:</p><p><strong>1.4. Operation</strong></p><pre><code>The Header Checksum provides a verification that the information used
in processing internet datagram has been transmitted correctly.  The
data may contain errors.  If the header checksum fails, the internet
datagram is discarded at once by the entity which detects the error.</code></pre><p><strong>3.1. Internet Header Format</strong></p><pre><code>Header Checksum:  16 bits

  A checksum on the header only.  Since some header fields change
  (e.g., time to live), this is recomputed and verified at each point
  that the internet header is processed.

  The checksum algorithm is:

    The checksum field is the 16 bit one&#39;s complement of the one&#39;s
    complement sum of all 16 bit words in the header.  For purposes of
    computing the checksum, the value of the checksum field is zero.

  This is a simple to compute checksum and experimental evidence
  indicates it is adequate, but it is provisional and may be replaced
  by a CRC procedure, depending on further experience.</code></pre><p><strong>3.2. Discussion</strong></p><pre><code>Checksum

  The internet header checksum is recomputed if the internet header is
  changed.  For example, a reduction of the time to live, additions or
  changes to internet options, or due to fragmentation.  This checksum
  at the internet level is intended to protect the internet header
  fields from transmission errors.

  There are some applications where a few data bit errors are
  acceptable while retransmission delays are not.  If the internet
  protocol enforced data correctness such applications could not be
  supported.</code></pre><p>For implementations of the Internet Checksum, refer to <a href="https://tools.ietf.org/html/rfc1071">RFC 1071</a> <code>Computing the Internet Checksum</code> along with its <a href="https://www.rfc-editor.org/errata_search.php?rfc=1071">Errata</a>, <a href="https://tools.ietf.org/html/rfc1141">RFC 1141</a> <code>Incremental Updating of the Internet Checksum</code> and <a href="https://tools.ietf.org/html/rfc1624">RFC 1624</a> <code>Computation of the Internet Checksum via Incremental Update</code>, which corrects a mistake made in RFC 1141.</p><p>If you're interested in the UDP Checksum, refer to <a href="https://tools.ietf.org/html/rfc768">RFC 768</a> <code>User Datagram Protocol</code>, where you'll find:</p><pre><code>Checksum is the 16-bit one&#39;s complement of the one&#39;s complement sum of a
pseudo header of information from the IP header, the UDP header, and the
data,  padded  with zero octets  at the end (if  necessary)  to  make  a
multiple of two octets.

The pseudo  header  conceptually prefixed to the UDP header contains the
source  address,  the destination  address,  the protocol,  and the  UDP
length.   This information gives protection against misrouted datagrams.
This checksum procedure is the same as is used in TCP.

                  0      7 8     15 16    23 24    31
                 +--------+--------+--------+--------+
                 |          source address           |
                 +--------+--------+--------+--------+
                 |        destination address        |
                 +--------+--------+--------+--------+
                 |  zero  |protocol|   UDP length    |
                 +--------+--------+--------+--------+

If the computed  checksum  is zero,  it is transmitted  as all ones (the
equivalent  in one&#39;s complement  arithmetic).   An all zero  transmitted
checksum  value means that the transmitter  generated  no checksum  (for
debugging or for higher level protocols that don&#39;t care).</code></pre><p>Since RFC 768 indicates that, <em>"This checksum procedure is the same as is used in TCP."</em>, you might also want to have a look at <a href="https://tools.ietf.org/html/rfc793">RFC 793</a> <code>TRANSMISSION CONTROL PROTOCOL</code>, where the Checksum field is described as follows:</p><pre><code>Checksum:  16 bits

  The checksum field is the 16 bit one&#39;s complement of the one&#39;s
  complement sum of all 16 bit words in the header and text.  If a
  segment contains an odd number of header and text octets to be
  checksummed, the last octet is padded on the right with zeros to
  form a 16 bit word for checksum purposes.  The pad is not
  transmitted as part of the segment.  While computing the checksum,
  the checksum field itself is replaced with zeros.

  The checksum also covers a 96 bit pseudo header conceptually
  prefixed to the TCP header.  This pseudo header contains the Source
  Address, the Destination Address, the Protocol, and TCP length.
  This gives the TCP protection against misrouted segments.  This
  information is carried in the Internet Protocol and is transferred
  across the TCP/Network interface in the arguments or results of
  calls by the TCP on the IP.

                   +--------+--------+--------+--------+
                   |           Source Address          |
                   +--------+--------+--------+--------+
                   |         Destination Address       |
                   +--------+--------+--------+--------+
                   |  zero  |  PTCL  |    TCP Length   |
                   +--------+--------+--------+--------+

    The TCP Length is the TCP header length plus the data length in
    octets (this is not an explicitly transmitted quantity, but is
    computed), and it does not count the 12 octets of the pseudo
    header.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '17, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-64091" class="comments-container"></div><div id="comment-tools-64091" class="comment-tools"></div><div class="clear"></div><div id="comment-64091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

